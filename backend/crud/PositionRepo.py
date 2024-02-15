from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Position
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Position)):
    @classmethod
    async def get_position_by_id(cls, session: AsyncSession, record_id: int) -> "Position":
        res = await session.execute(select(cls.Position).where(Position.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_positions(cls, session: AsyncSession) -> "Position":
        res = await session.execute(select(cls.Position))
        return res.scalar().all()

    @classmethod
    async def create_position(cls, session: AsyncSession, **kwargs) -> "Position":
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_position(cls, session: AsyncSession, position_id: int):
        client_to_delete = await session.execute(select(Position).where(Position.id == position_id))
        client_to_delete = client_to_delete.scalar_one()
        await session.delete(client_to_delete)
        await session.commit()
