from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ClientType
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ClientType)):
    @classmethod
    async def get_client_type_by_id(cls, session: AsyncSession, record_id: int) -> "ClientType":
        res = await session.execute(select(cls.ClientType).where(ClientType.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_client_type(cls, session: AsyncSession) -> "ClientType":
        res = await session.execute(select(cls.ClientType))
        return res.scalar().all()

    @classmethod
    async def create_client_type(cls, session: AsyncSession, **kwargs) -> "ClientType":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client_type(cls, session: AsyncSession, client_type_id: int):
        res = await session.execute(select(ClientType).where(ClientType.id == client_type_id))
        clientType_to_delete = res.scalar_one()
        await session.delete(clientType_to_delete)
        await session.commit()
