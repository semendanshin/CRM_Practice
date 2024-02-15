from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import DevicesOperationIn
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(DevicesOperationIn)):
    @classmethod
    async def get_device_operation_in_by_id(cls, session: AsyncSession, record_id: int) -> "DevicesOperationIn":
        res = await session.execute(select(cls.DevicesOperationIn).where(DevicesOperationIn.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_device_operation_in(cls, session: AsyncSession) -> "DevicesOperationIn":
        res = await session.execute(select(cls.DevicesOperationIn))
        return res.scalar().all()

    @classmethod
    async def create_device_operation_in(cls, session: AsyncSession, **kwargs) -> "DevicesOperationIn":
        instance = cls.DevicesOperationIn(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_device_operation_in(cls, session: AsyncSession, devices_operation_in_id: int):
        res = await session.execute(select(DevicesOperationIn).where(DevicesOperationIn.id == devices_operation_in_id))
        devices_operation_in_to_delete = res.scalar_one()
        await session.delete(devices_operation_in_to_delete)
        await session.commit()
