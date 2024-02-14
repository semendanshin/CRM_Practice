from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TMCOperationOut
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TMCOperationOut)):
    @classmethod
    async def get_tmc_operation_out_by_id(cls, session: AsyncSession, record_id: int) -> "TMCOperationOut":
        res = await session.execute(select(cls.TMCOperationOut).where(TMCOperationOut.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_tmc_operation_out(cls, session: AsyncSession) -> "TMCOperationOut":
        res = await session.execute(select(cls.TMCOperationOut))
        return res.scalar().all()

    @classmethod
    async def create_tmc_operation_out(cls, session: AsyncSession, **kwargs) -> "TMCOperationOut":
        instance = cls.TMCOperationOut(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_tmc_operation_out(cls, session: AsyncSession, tmc_operation_out_id: int):
        res = await session.execute(select(TMCOperationOut).where(TMCOperationOut.id == tmc_operation_out_id))
        tmc_operation_out_to_delete = res.scalar_one()
        await session.delete(tmc_operation_out_to_delete)
        await session.commit()
