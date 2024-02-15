from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Authorization, Employee, BotAuthorization, Ticket
from .CrudFactory import CrudFactory


class AuthRepo(CrudFactory(Authorization)):
    @classmethod
    async def get_by_refresh_token(cls, session: AsyncSession, refresh_token) -> Authorization:
        res = await session.execute(
            cls.model.__table__.select().where(cls.model.refresh_token == refresh_token)
        )
        return res.scalar().first()
    
    @classmethod
    async def get_by_user_id(cls, session: AsyncSession, user_id) -> Authorization:
        res = await session.execute(
            cls.model.__table__.select().where(cls.model.user_id == user_id)
        )
        return res.scalar().first()
    
    @classmethod
    async def get_by_access_token(cls, session: AsyncSession, access_token) -> Authorization:
        res = await session.execute(
            cls.model.__table__.select().where(cls.model.access_token == access_token)
        )
        return res.scalar().first()

    @classmethod
    async def delete_by_user_id(cls, session: AsyncSession, user_id):
        await session.execute(
            cls.model.__table__.delete().where(cls.model.user_id == user_id)
        )
        await session.commit()


class BotAuthRepo(CrudFactory(BotAuthorization)):
    @classmethod
    async def get_by_token(cls, session: AsyncSession, token) -> BotAuthorization:
        res = await session.execute(
            select(cls.model).where(cls.model.token==token)
        )
        return res.scalar()

    @classmethod
    async def get_by_client_id(cls, session: AsyncSession, client_id) -> BotAuthorization:
        res = await session.execute(
            select(cls.model).where(cls.model.client_id==client_id)
        )
        return res.scalar()

    @classmethod
    async def delete_by_token(cls, session: AsyncSession, token):
        await session.execute(
            cls.model.__table__.delete().where(cls.model.token == token)
        )
        await session.commit()


class TicketRepo(CrudFactory(Ticket)):
    @classmethod
    async def get_by_client_id(cls, session: AsyncSession, client_id: int) -> Sequence[Ticket]:
        if not isinstance(client_id, int):
            raise TypeError("client_id must be an integer")
        res = await session.execute(
            select(cls.model).where(cls.model.client_id == client_id)
        )
        return res.scalars().all()


employee_repo = CrudFactory(Employee)
auth_repo = AuthRepo
bot_auth_repo = BotAuthRepo
ticket_repo = TicketRepo
