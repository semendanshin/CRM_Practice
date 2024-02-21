from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .CrudFactory import CrudFactory
from db.models import BotAuthorization

from schemas.bot_authorization import BotAuthorizationCreate, BotAuthorizationUpdate, BotAuthorizationResponse


class BotAuthRepo(
    CrudFactory(
        BotAuthorization,
        BotAuthorizationUpdate,
        BotAuthorizationCreate,
        BotAuthorizationResponse
    )
):
    @classmethod
    async def get_by_token(cls, session: AsyncSession, token) -> BotAuthorizationResponse | None:
        res = await session.execute(
            select(cls.model).where(cls.model.token == token)
        )
        obj = res.scalar_one_or_none()
        return cls.get_schema.model_validate(obj) if obj else None

    @classmethod
    async def get_by_client_id(cls, session: AsyncSession, client_id) -> BotAuthorizationResponse | None:
        res = await session.execute(
            select(cls.model).where(cls.model.client_id == client_id)
        )
        obj = res.scalar_one_or_none()
        return cls.get_schema.model_validate(obj) if obj else None

    @classmethod
    async def delete_by_token(cls, session: AsyncSession, token):
        await session.execute(
            cls.model.__table__.delete().where(cls.model.token == token)
        )
        await session.commit()