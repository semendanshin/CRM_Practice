from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TMCOperationIn
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TMCOperationIn)):
    @classmethod
    async def get_tmc_operation_in_by_id(cls, session: AsyncSession, record_id: int) -> "TMCOperationIn":
        res = await session.execute(select(cls.TMCOperationIn).where(TMCOperationIn.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_tmc_operation_in(cls, session: AsyncSession) -> "TMCOperationIn":
        res = await session.execute(select(cls.TMCOperationIn))
        return res.scalar().all()

    @classmethod
    async def create_tmc_operation_in(cls, session: AsyncSession, **kwargs) -> "TMCOperationIn":
        instance = cls.TMCOperationIn(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_tmc_operation_in(cls, session: AsyncSession, tmc_operation_in_id: int):
        res = await session.execute(select(TMCOperationIn).where(TMCOperationIn.id == tmc_operation_in_id))
        tmc_operation_in_to_delete = res.scalar_one()
        await session.delete(tmc_operation_in_to_delete)
        await session.commit()
