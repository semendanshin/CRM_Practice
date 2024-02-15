from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TMCOperationMove
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TMCOperationMove)):
    @classmethod
    async def get_tmc_operation_move_by_id(cls, session: AsyncSession, record_id: int) -> "TMCOperationMove":
        res = await session.execute(select(cls.TMCOperationMove).where(TMCOperationMove.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_tmc_operation_move(cls, session: AsyncSession) -> "TMCOperationMove":
        res = await session.execute(select(cls.TMCOperationMove))
        return res.scalar().all()

    @classmethod
    async def create_tmc_operation_move(cls, session: AsyncSession, **kwargs) -> "TMCOperationMove":
        instance = cls.TMCOperationMove(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_tmc_operation_move(cls, session: AsyncSession, tmc_operation_move_id: int):
        res = await session.execute(select(TMCOperationMove).where(TMCOperationMove.id == tmc_operation_move_id))
        tmc_operation_move_to_id = res.scalar_one()
        await session.delete(tmc_operation_move_to_id)
        await session.commit()
