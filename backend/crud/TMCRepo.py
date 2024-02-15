from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TMC
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TMC)):
    @classmethod
    async def get_tmc_by_id(cls, session: AsyncSession, record_id: int) -> "TMC":
        res = await session.execute(select(cls.TMC).where(TMC.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_tmc(cls, session: AsyncSession) -> "TMC":
        res = await session.execute(select(cls.TMC))
        return res.scalar().all()

    @classmethod
    async def create_tmc(cls, session: AsyncSession, **kwargs) -> "TMC":
        instance = cls.TMC(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_tmc(cls, session: AsyncSession, tmc_id: int):
        res = await session.execute(select(TMC).where(TMC.id == tmc_id))
        tmc_to_delete = res.scalar_one()
        await session.delete(tmc_to_delete)
        await session.commit()
