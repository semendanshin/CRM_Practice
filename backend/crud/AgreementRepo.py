from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Agreement
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Agreement)):
    @classmethod
    async def get_group_by_id(cls, session: AsyncSession, record_id: int) -> "Agreement":
        res = await session.execute(select(cls.Agreement).where(Agreement.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_groups(cls, session: AsyncSession) -> "Agreement":
        res = await session.execute(select(cls.Agreement))
        return res.scalar().all()

    @classmethod
    async def create_group(cls, session: AsyncSession, **kwargs) -> "Agreement":
        instance = cls.Agreement(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_group(cls, session: AsyncSession, agreement_id: int):
        res = await session.execute(select(Agreement).where(Agreement.id == agreement_id))
        agreement_to_delete = res.scalar_one()
        await session.delete(agreement_to_delete)
        await session.commit()
