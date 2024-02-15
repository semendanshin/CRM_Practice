from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Observer
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Observer)):
    @classmethod
    async def get_observer_id(cls, session: AsyncSession, record_id: int) -> "Observer":
        res = await session.execute(select(cls.Observer).where(Observer.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_observers(cls, session: AsyncSession) -> "Observer":
        res = await session.execute(select(cls.Observer))
        return res.scalar().all()

    @classmethod
    async def create_observer(cls, session: AsyncSession, **kwargs) -> "Observer":
        instance = cls.Observer(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_observer(cls, session: AsyncSession, observer_id: int):
        res = await session.execute(select(Observer).where(Observer.id == observer_id))
        observer_to_delete = res.scalar_one()
        await session.delete(observer_to_delete)
        await session.commit()
