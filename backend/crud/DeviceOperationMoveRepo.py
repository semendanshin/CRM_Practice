from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import DeviceOperationMove
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(DeviceOperationMove)):
    @classmethod
    async def get_device_operation_move_by_id(cls, session: AsyncSession, record_id: int) -> "DeviceOperationMove":
        res = await session.execute(select(cls.DeviceOperationMove).where(DeviceOperationMove.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_device_operation_move(cls, session: AsyncSession) -> "DeviceOperationMove":
        res = await session.execute(select(cls.DeviceOperationMove))
        return res.scalar().all()

    @classmethod
    async def create_device_operation_move(cls, session: AsyncSession, **kwargs) -> "DeviceOperationMove":
        instance = cls.DeviceOperationMove(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_device_operation_move(cls, session: AsyncSession, device_operation_move_id: int):
        res = await session.execute(select(DeviceOperationMove).where(DeviceOperationMove.id == device_operation_move_id))
        device_operation_move_to_delete = res.scalar_one()
        await session.delete(device_operation_move_to_delete)
        await session.commit()
