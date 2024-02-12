from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepo:
    model = None

    async def get(self, session: AsyncSession, id: int):
        res = await session.execute(select(self.model).where(self.model.id == id))
        return res.scalar().first()

    async def get_all(self, session: AsyncSession):
        res = await session.execute(select(self.model))
        return res.scalar().all()

    async def create(self, session: AsyncSession, **kwargs):
        instance = self.model(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    async def update(self, session: AsyncSession, id: int, **kwargs):
        await session.execute(select(self.model).where(self.model.id == id))
        await session.commit()

    async def delete(self, session: AsyncSession, id: int):
        await session.execute(select(self.model).where(self.model.id == id))
        await session.commit()