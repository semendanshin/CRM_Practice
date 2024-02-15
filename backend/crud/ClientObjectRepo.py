from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ClientObject
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ClientObject)):
    @classmethod
    async def get_client_object_by_id(cls, session: AsyncSession, record_id: int) -> "ClientObject":
        res = await session.execute(select(cls.ClientObject).where(ClientObject.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_client_objects(cls, session: AsyncSession) -> "ClientObject":
        res = await session.execute(select(cls.ClientObject))
        return res.scalar().all()

    @classmethod
    async def create_client_object(cls, session: AsyncSession, **kwargs) -> "ClientObject":
        instance = cls.ClientObject(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client_object(cls, session: AsyncSession, client_object_id: int):
        res = await session.execute(select(ClientObject).where(ClientObject.id == client_object_id))
        client_object_to_delete = res.scalar_one()
        await session.delete(client_object_to_delete)
        await session.commit()
