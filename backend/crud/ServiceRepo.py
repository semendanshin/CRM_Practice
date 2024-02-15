from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Service
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Service)):
    @classmethod
    async def get_service_by_id(cls, session: AsyncSession, record_id: int) -> "Service":
        res = await session.execute(select(cls.Service).where(Service.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_services(cls, session: AsyncSession) -> "Service":
        res = await session.execute(select(cls.Service))
        return res.scalar().all()

    @classmethod
    async def create_service(cls, session: AsyncSession, **kwargs) -> "Service":
        instance = cls.Service(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_service(cls, session: AsyncSession, service_id: int):
        res = await session.execute(select(Service).where(Service.id == service_id))
        service_to_delete = res.scalar_one()
        await session.delete(service_to_delete)
        await session.commit()
