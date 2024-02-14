from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Group
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Group)):
    @classmethod
    async def get_group_by_id(cls, session: AsyncSession, record_id: int) -> "Group":
        res = await session.execute(select(cls.Position).where(Group.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_groups(cls, session: AsyncSession) -> "Group":
        res = await session.execute(select(cls.Group))
        return res.scalar().all()

    @classmethod
    async def create_group(cls, session: AsyncSession, **kwargs) -> "Group":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_group(cls, session: AsyncSession, group_id: int):
        client_to_delete = await session.execute(select(Group).where(Group.id == group_id))
        client_to_delete = client_to_delete.scalar_one()
        await session.delete(client_to_delete)
        await session.commit()
