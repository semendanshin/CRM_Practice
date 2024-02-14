from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import SLA
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(SLA)):
    @classmethod
    async def get_sla_by_id(cls, session: AsyncSession, record_id: int) -> "SLA":
        res = await session.execute(select(cls.SLA).where(SLA.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_sla(cls, session: AsyncSession) -> "SLA":
        res = await session.execute(select(cls.SLA))
        return res.scalar().all()

    @classmethod
    async def create_sla(cls, session: AsyncSession, **kwargs) -> "SLA":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_sla(cls, session: AsyncSession, sla_id: int):
        client_to_delete = await session.execute(select(SLA).where(SLA.id == sla_id))
        client_to_delete = client_to_delete.scalar_one()
        await session.delete(client_to_delete)
        await session.commit()
