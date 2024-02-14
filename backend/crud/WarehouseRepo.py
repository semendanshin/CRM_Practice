from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Warehouse
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Warehouse)):
    @classmethod
    async def get_warehouse_by_id(cls, session: AsyncSession, record_id: int) -> "Warehouse":
        res = await session.execute(select(cls.Warehouse).where(Warehouse.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_warehouses(cls, session: AsyncSession) -> "Warehouse":
        res = await session.execute(select(cls.Warehouse))
        return res.scalar().all()

    @classmethod
    async def create_warehouse(cls, session: AsyncSession, **kwargs) -> "Warehouse":
        instance = cls.Warehouse(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_warehouse(cls, session: AsyncSession, warehouse_id: int):
        res = await session.execute(select(Warehouse).where(Warehouse.id == warehouse_id))
        warehouse_to_delete = res.scalar_one()
        await session.delete(warehouse_to_delete)
        await session.commit()
