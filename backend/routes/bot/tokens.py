from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from db.models import Client, BotAuthorization
from schemas import ClientResponse

from .exceptions import TokenEmptyException, TokenNotFoundException

from crud import BotAuthRepo, ClientRepo

from uuid import uuid4

from logging import getLogger

logger = getLogger(__name__)


async def check_token(
        token: str,
        session: AsyncSession, ) -> ClientResponse:

    if not token:
        raise TokenEmptyException

    # find BotAuthorization by token and return Client with same id
    bot_authorization = await BotAuthRepo.get_by_token(session, token)

    if bot_authorization is None:
        raise TokenNotFoundException

    print(bot_authorization.client_id)

    client = await ClientRepo.get(session, bot_authorization.client_id)

    return client


async def create_token(
        client_id: int,
        session: AsyncSession, ) -> BotAuthorization:

    instance = await BotAuthRepo.get_by_client_id(session=session, client_id=client_id)

    token = str(uuid4())
    # logger.info(token)
    # logger.info(client_id)
    #
    # print(token, client_id)

    if instance:
        # print('updating')
        instance = await BotAuthRepo.update(
            session=session,
            record_id=instance.id,
            token=token,
        )
    else:
        instance = await BotAuthRepo.create(session=session, client_id=client_id, token=token)

    return instance

