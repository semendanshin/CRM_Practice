from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


def CrudFactory(model):
    class AbstractRepo:
        model = None

        @classmethod
        async def get(cls, session: AsyncSession, record_id: int) -> "model":
            res = await session.execute(select(cls.model).where(cls.model.id == record_id))
            return res.scalar().first()

        @classmethod
        async def get_all(cls, session: AsyncSession) -> "model":
            res = await session.execute(select(cls.model))
            return res.scalar().all()

        @classmethod
        async def create(cls, session: AsyncSession, **kwargs) -> "model":
            instance = cls.model(**kwargs)
            session.add(instance)
            await session.commit()
            return instance

        @classmethod
        async def update(cls, session: AsyncSession, record_id: int, **kwargs):
            instance = await session.execute(select(cls.model).where(cls.model.id == record_id))
            instance = instance.scalars().first()
            for key, value in kwargs.items():
                if value is not None:
                    setattr(instance, key, value)
            await session.commit()

        @classmethod
        async def delete(cls, session: AsyncSession, record_id: int):
            instance = await session.execute(select(cls.model).where(cls.model.id == record_id))
            await session.delete(instance)
            await session.commit()

    AbstractRepo.model = model
    return AbstractRepo
