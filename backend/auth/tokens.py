import jwt
import datetime
import json

from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Employee, Authorization
from backend.conf import JWT_SECRET, ACCESS_EXPIRE_DAYS, REFRESH_EXPIRE_DAYS

from .exceptions import EmptyTokenError, InvalidTokenError, ExpiredTokenException

from backend.crud.AuthRepo import AuthRepo
from backend.crud.EmployeeRepo import EmployeeRepo
from ..db import get_session


class Result:
    def __init__(self, status, data=None):
        self.status = status
        self.data = data


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


def generate_tokens(employee_id: int, received_tokens: dict[str, str] = None) -> dict[str, str]:
    """
    Generate tokens for user
    :param employee_id:
    :param received_tokens: by default None
    :return: tokens dict
    {
        'access': str,
        'refresh': str,
    }
    """
    if received_tokens is None:
        received_tokens = {}

    result = check_token(received_tokens=received_tokens)
    # print(result.status, result.data)

    if result.status == 'ok':
        employee_id = result.data
        user = User.objects.get_or_none(id=user_id)

    user = User.objects.get_or_none(phone=phone)

    if result.data in ['Invalid token', 'Access token expired', 'Refresh token expired'] or result.status == 'ok':
        Token.objects.get_or_none(user=user).delete()

    tokens = {
        'access': jwt.encode(
            {
                'user_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=JWT_SECRET,
            algorithm="HS256",
        ),
        'refresh': jwt.encode(
            {
                'user_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=JWT_SECRET,
            algorithm="HS256",
        ),
    }
    Token.objects.create(user=user, refresh=tokens['refresh'], access=tokens['access'])
    return tokens


@router.post("/refresh", response_model=Result)
async def refresh_tokens(received_tokens: Authorization = None,
                         session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    """
    Refresh tokens
    :param session:
    :param received_tokens: tokens
    :return: new tokens
    """
    if not received_tokens:
        raise EmptyTokenError('No token provided')

    exist_token = await AuthRepo.get_by_refresh(
        session,
        received_tokens.refresh_token
    )

    if not exist_token:
        raise InvalidTokenError('No tokens for this user')

    try:
        refresh = jwt.decode(received_tokens['refresh'],
                             key=JWT_SECRET,
                             algorithms="HS256",
                             verify=False)
    except jwt.exceptions.PyJWTError as e:
        raise InvalidTokenError(e)

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') < datetime.datetime.utcnow():
        raise ExpiredTokenException('Refresh token expired')

    user = EmployeeRepo.get_by_id(session=get_session(), id=refresh['employee_id'])

    tokens = {
        'access': jwt.encode(
            {
                'employee_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=ACCESS_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=JWT_SECRET,
            algorithm="HS256",
        ),
        'refresh': jwt.encode(
            {
                'employee_id': user.id,
                'expires_on': (datetime.datetime.utcnow() +
                               datetime.timedelta(days=REFRESH_EXPIRE_DAYS)).strftime('%Y-%m-%d %H:%M:%S.%f'),
            },
            key=JWT_SECRET,
            algorithm="HS256",
        ),
    }

    exist_token.refresh = tokens['refresh']
    exist_token.access = tokens['access']
    await exist_token.save()
    return exist_token


def check_token(session: AsyncSession, received_tokens: dict[str, str] = None) -> Result:
    """
    Check token
    :param session:
    :param received_tokens: tokens
    :return: user id
    """
    if received_tokens is None:
        raise

    if not received_tokens:
        return Result('error', 'No token provided')

    received_tokens = json.loads(str(received_tokens))

    try:
        access = jwt.decode(received_tokens['access'], "redrum", algorithms="HS256", verify=False)
        refresh = jwt.decode(received_tokens['refresh'], "redrum", algorithms="HS256", verify=False)
    except jwt.exceptions.PyJWTError as e:
        return Result('error', e)

    user = User.objects.get_or_none(id=access['user_id'])
    exist_token = Token.objects.get_or_none(user=user)
    print(user)

    if not exist_token:
        return Result('error', 'No tokens for this user')

    try:
        exist_access = jwt.decode(exist_token.access, "redrum", algorithms="HS256", verify=False)
        exist_refresh = jwt.decode(exist_token.refresh, "redrum", algorithms="HS256", verify=False)
    except jwt.exceptions.PyJWTError as e:
        return Result('error', e)

    if access['user_id'] != refresh['user_id'] or \
            access['user_id'] != exist_access['user_id'] or \
            refresh['user_id'] != exist_refresh['user_id'] or \
            access != exist_access or \
            refresh != exist_refresh:
        return Result('error', 'Invalid token')

    if datetime.datetime.strptime(access['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_access['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        return Result('error', 'Access token expired')

    if datetime.datetime.strptime(refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f') \
            < datetime.datetime.strptime(exist_refresh['expires_on'], '%Y-%m-%d %H:%M:%S.%f'
                                         ):
        return Result('error', 'Refresh token expired')

    return Result('ok', access['user_id'])
