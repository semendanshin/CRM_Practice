from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from db.models import Client, BotAuthorization

from .exceptions import TokenEmptyException, TokenNotFoundException

from crud import bot_auth_repo

from uuid import uuid4

from logging import getLogger

logger = getLogger(__name__)


async def check_token(
        token: str,
        session: AsyncSession,
) -> Client:
    if not token:
        raise TokenEmptyException

    # find BotAuthorization by token and return Client with same id
    bot_authorization = await bot_auth_repo.get_by_token(session, token)

    await session.refresh(bot_authorization, attribute_names=['client'])

    if bot_authorization is None:
        raise TokenNotFoundException

    return bot_authorization.client


async def create_token(
        client_id: int,
        session: AsyncSession, ) -> BotAuthorization:

    instance = await bot_auth_repo.get_by_client_id(session=session, client_id=client_id)

    token = str(uuid4())
    logger.info(token)
    logger.info(client_id)

    print(token, client_id)

    if instance:
        print('updating')
        await bot_auth_repo.update(
            session=session,
            record_id=instance.id,
            token=token,
        )
    else:
        instance = await bot_auth_repo.create(session=session, client_id=client_id, token=token)

    await session.refresh(instance, attribute_names=['token'])

    return instance

