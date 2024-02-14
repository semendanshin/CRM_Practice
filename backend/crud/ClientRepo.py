from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Client
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Client)):
    @classmethod
    async def get_client_by_id(cls, session: AsyncSession, record_id: int) -> "Client":
        res = await session.execute(select(cls.Client).where(Client.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_clients(cls, session: AsyncSession) -> "Client":
        res = await session.execute(select(cls.Client))
        return res.scalar().all()

    @classmethod
    async def create_client(cls, session: AsyncSession, **kwargs) -> "Client":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_client(cls, session: AsyncSession, client_id: int):
        client_to_delete = await session.execute(select(Client).where(Client.id == client_id))
        client_to_delete = client_to_delete.scalar_one()
        await session.delete(client_to_delete)
        await session.commit()
