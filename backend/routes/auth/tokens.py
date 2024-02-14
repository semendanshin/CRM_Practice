from typing import Optional, Union

import jwt
import datetime

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.auth import AuthorizationCreate
from routes.auth.exceptions import (
    TokenInvalidException,
    TokenExpiredException,
    TokenNotFoundException,
    TokenEmptyException,
)
from config import config
from crud import auth_repo, employee_repo
from db.models import Employee

from logging import getLogger

logger = getLogger(__name__)


class Tokens(BaseModel):
    access: str
    refresh: str


async def create_tokens(session: AsyncSession,
                  employee_id: int,
                  received_tokens: Optional[Tokens] = None) -> Tokens:
    """
    Generate tokens for user
    :param session:
    :param employee_id:
    :param received_tokens: by default None
    :return: tokens dict
    {
        'access': str,
        'refresh': str,
    }
    """

    try:
        user = await check_token(session, received_tokens=received_tokens)
    except Union[TokenEmptyException, TokenNotFoundException]:
        user = await employee_repo.get_by_id(session, employee_id)
    except Union[TokenInvalidException, TokenExpiredException]:
        user = await employee_repo.get_by_id(session, employee_id)
        await auth_repo.delete_by_user_id(session, user.id)

    tokens = AuthorizationCreate(
        access=jwt.encode(
            {
                'user_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET,
            algorithm="HS256",
        ),
        refresh=jwt.encode(
            {
                'user_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET,
            algorithm="HS256",
        ),
        user_id=user.id
    )

    await auth_repo.create(
        session,
        tokens
    )

    return Tokens(
        access=tokens.access_token,
        refresh=tokens.refresh_token
    )


async def refresh_tokens(session: AsyncSession,
                         received_tokens: Tokens = None) -> Tokens:
    """
    Refresh tokens
    :param session:
    :param received_tokens: tokens
    :return: new tokens
    """
    if not received_tokens:
        raise TokenEmptyException

    exist_token = await auth_repo.get_by_refresh_token(
        session,
        received_tokens.refresh_token
    )

    if not exist_token:
        raise TokenNotFoundException

    try:
        refresh = jwt.decode(received_tokens.refresh_token,
                             key=config.JWT_SECRET,
                             algorithms="HS256",
                             verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.utcnow():
        raise TokenExpiredException

    user = await employee_repo.get(session, refresh['employee_id'])

    tokens = {
        'access': jwt.encode(
            {
                'employee_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET,
            algorithm="HS256",
        ),
        'refresh': jwt.encode(
            {
                'employee_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET,
            algorithm="HS256",
        ),
    }

    exist_token.refresh = tokens['refresh']
    exist_token.access = tokens['access']
    await exist_token.save()
    return exist_token


async def check_token(session: AsyncSession,
                received_tokens: Optional[Tokens] = None) -> Employee:
    """
    Check token
    :param session:
    :param received_tokens: tokens
    :return: user id
    """
    if not received_tokens:
        raise TokenEmptyException('No token provided')

    try:
        access = jwt.decode(received_tokens['access'], "redrum", algorithms="HS256", verify=False)
        refresh = jwt.decode(received_tokens['refresh'], "redrum", algorithms="HS256", verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException('Invalid token')

    user = await employee_repo.get(session, access['employee_id'])
    exist_token = await auth_repo.get_by_user_id(session, user.id)

    if not exist_token:
        raise

    try:
        exist_access = jwt.decode(exist_token.access, "redrum", algorithms="HS256", verify=False)
        exist_refresh = jwt.decode(exist_token.refresh, "redrum", algorithms="HS256", verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException('Invalid token')

    if access['user_id'] != refresh['user_id'] or \
            access['user_id'] != exist_access['user_id'] or \
            refresh['user_id'] != exist_refresh['user_id'] or \
            access != exist_access or \
            refresh != exist_refresh:
        raise TokenInvalidException('Invalid token')

    if datetime.datetime.strptime(access['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_access['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        raise TokenExpiredException('Access token expired')

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        raise TokenExpiredException('Refresh token expired')

    return user
