from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Authorization
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Authorization)):
    @classmethod
    async def get_authorization_by_id(cls, session: AsyncSession, record_id: int) -> "Authorization":
        res = await session.execute(select(cls.Authorization).where(Authorization.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_authorizations(cls, session: AsyncSession) -> "Authorization":
        res = await session.execute(select(cls.Authorization))
        return res.scalar().all()

    @classmethod
    async def create_authorization(cls, session: AsyncSession, **kwargs) -> "Authorization":
        instance = cls.Authorization(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_authorization(cls, session: AsyncSession, authorization_id: int):
        res = await session.execute(select(Authorization).where(Authorization.id == authorization_id))
        authorization_to_delete = res.scalar_one()
        await session.delete(authorization_to_delete)
        await session.commit()
