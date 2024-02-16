from sqlalchemy.ext.asyncio import AsyncSession

from .CrudFactory import  CrudFactory
from db.models import Authorization
from schemas.authorization import AuthorizationCreate, AuthorizationUpdate, AuthorizationResponse


class AuthorizationRepo(
    CrudFactory(
        Authorization,
        AuthorizationUpdate,
        AuthorizationCreate,
        AuthorizationResponse,
    )
):
    @classmethod
    async def get_by_refresh_token(cls, session: AsyncSession, refresh_token) -> AuthorizationResponse:
        res = await session.execute(
            cls.model.__table__.select().where(cls.model.refresh_token == refresh_token)
        )
        return res.scalar().first()

    @classmethod
    async def get_by_user_id(cls, session: AsyncSession, user_id) -> AuthorizationResponse:
        res = await session.execute(
            cls.model.__table__.select().where(cls.model.user_id == user_id)
        )
        return res.scalar().first()

    @classmethod
    async def get_by_access_token(cls, session: AsyncSession, access_token) -> AuthorizationResponse:
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
