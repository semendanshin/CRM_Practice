from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Devices
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Devices)):
    @classmethod
    async def get_device_by_id(cls, session: AsyncSession, record_id: int) -> "Devices":
        res = await session.execute(select(cls.Devices).where(Devices.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_devices(cls, session: AsyncSession) -> "Devices":
        res = await session.execute(select(cls.Devices))
        return res.scalar().all()

    @classmethod
    async def create_device(cls, session: AsyncSession, **kwargs) -> "Devices":
        instance = cls.Devices(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_device(cls, session: AsyncSession, device_id: int):
        res = await session.execute(select(Devices).where(Devices.id == device_id))
        device_to_delete = res.scalar_one()
        await session.delete(device_to_delete)
        await session.commit()
