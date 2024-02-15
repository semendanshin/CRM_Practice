from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import DeviceOperationOut
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(DeviceOperationOut)):
    @classmethod
    async def get_device_operation_out_by_id(cls, session: AsyncSession, record_id: int) -> "DeviceOperationOut":
        res = await session.execute(select(cls.DeviceOperationOut).where(DeviceOperationOut.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_devices_operation_out(cls, session: AsyncSession) -> "DeviceOperationOut":
        res = await session.execute(select(cls.DeviceOperationOut))
        return res.scalar().all()

    @classmethod
    async def create_device_operation_out(cls, session: AsyncSession, **kwargs) -> "DeviceOperationOut":
        instance = cls.DeviceOperationOut(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_device_operation_out(cls, session: AsyncSession, device_operation_out_id: int):
        res = await session.execute(select(DeviceOperationOut).where(DeviceOperationOut.id == device_operation_out_id))
        device_operation_out = res.scalar_one()
        await session.delete(device_operation_out)
        await session.commit()
