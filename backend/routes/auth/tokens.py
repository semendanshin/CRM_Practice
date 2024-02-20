import datetime
from logging import getLogger
from typing import Optional

import jwt
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from config import config
from crud import AuthorizationRepo, EmployeeRepo
from db.models import Employee
from routes.auth.exceptions import (
    TokenInvalidException,
    TokenExpiredException,
    TokenNotFoundException,
    TokenEmptyException,
)
from schemas.authorization import AuthorizationCreate

logger = getLogger(__name__)


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


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
    except (TokenEmptyException, TokenNotFoundException):
        user = await EmployeeRepo.get(session, employee_id)
    except (TokenInvalidException, TokenExpiredException):
        user = await EmployeeRepo.get(session, employee_id)
        await AuthorizationRepo.delete_by_user_id(session, user.id)

    tokens = AuthorizationCreate(
        access_token=jwt.encode(
            {
                'obj': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET.get_secret_value(),
            algorithm="HS256",
        ),
        refresh_token=jwt.encode(
            {
                'obj': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET.get_secret_value(),
            algorithm="HS256",
        ),
        employee_id=user.id
    )

    tokens = await AuthorizationRepo.create(
        session,
        **tokens.model_dump(),
    )

    return tokens


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

    exist_token = await AuthorizationRepo.get_by_refresh_token(
        session,
        received_tokens.refresh_token
    )

    if not exist_token:
        raise TokenNotFoundException

    try:
        refresh = jwt.decode(received_tokens.refresh_token,
                             key=config.JWT_SECRET.get_secret_value(),
                             algorithms="HS256",
                             verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.utcnow():
        raise TokenExpiredException

    user = await EmployeeRepo.get(session, refresh['obj'])

    tokens = {
        'access': jwt.encode(
            {
                'obj': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET.get_secret_value(),
            algorithm="HS256",
        ),
        'refresh': jwt.encode(
            {
                'obj': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=config.REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=config.JWT_SECRET.get_secret_value(),
            algorithm="HS256",
        ),
    }

    tokens = await AuthorizationRepo.update(
        session,
        exist_token.id,
        access_token=tokens['access'],
        refresh_token=tokens['refresh'],
    )

    return tokens


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
        access = jwt.decode(received_tokens.access_token, config.JWT_SECRET.get_secret_value(), algorithms="HS256",
                            verify=False)
        refresh = jwt.decode(received_tokens.refresh_token, config.JWT_SECRET.get_secret_value(), algorithms="HS256",
                             verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException('Invalid token')

    user = await EmployeeRepo.get(session, access['obj'])
    exist_token = await AuthorizationRepo.get_by_employee_id(session, user.id)

    if not exist_token:
        raise

    try:
        exist_access = jwt.decode(exist_token.access_token, config.JWT_SECRET.get_secret_value(), algorithms="HS256",
                                  verify=False)
        exist_refresh = jwt.decode(exist_token.refresh_token, config.JWT_SECRET.get_secret_value(), algorithms="HS256",
                                   verify=False)
    except jwt.exceptions.PyJWTError as e:
        logger.error(f'Invalid token: {e}')
        raise TokenInvalidException('Invalid token')

    if access['obj'] != refresh['obj']:
        logger.error('Invalid token: obj mismatch in received tokens')
        raise TokenInvalidException('Invalid token')
    if access != exist_access:
        logger.error('Invalid token: access token mismatch')
    if refresh != exist_refresh:
        logger.error('Invalid token: refresh token mismatch')

    if datetime.datetime.strptime(access['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_access['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        raise TokenExpiredException('Access token expired')

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        raise TokenExpiredException('Refresh token expired')

    return user
