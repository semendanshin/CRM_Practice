from typing import TypeVar, Optional, TypeAlias, Generic, Type

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Schema = TypeVar("Schema", bound=BaseModel, covariant=True)
SQLModel = TypeVar("SQLModel", bound=declarative_base())


class AbstractRepo:
    model: SQLModel
    update_schema: Type[Schema]
    create_schema: Type[Schema]
    get_schema: Type[Schema]

    @classmethod
    async def get(cls, session: AsyncSession, record_id: int) -> Schema | None:
        res = await session.execute(select(cls.model).where(cls.model.id == record_id))
        obj = res.scalar_one()
        return cls.get_schema.model_validate(obj) if obj else None

    @classmethod
    async def get_all(cls, session: AsyncSession, offset: int = 0, limit: int = 100) -> list[Schema]:
        res = await session.execute(select(cls.model).offset(offset).limit(limit))
        objects = res.scalars().all()
        return [cls.get_schema.model_validate(obj) for obj in objects]

    @classmethod
    async def get_filtered_by(cls, session: AsyncSession, **kwargs) -> list[Schema]:
        res = await session.execute(select(cls.model).filter_by(**kwargs))
        objects = res.scalars().all()
        return [cls.get_schema.model_validate(obj) for obj in objects]

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs) -> Schema:
        instance = cls.model(**kwargs)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return cls.get_schema.model_validate(instance)

    @classmethod
    async def update(cls, session: AsyncSession, record_id: int, **kwargs) -> Schema:
        clean_kwargs = {key: value for key, value in kwargs.items() if value is not None}
        await session.execute(update(cls.model).where(cls.model.id == record_id).values(**clean_kwargs))
        await session.commit()
        return await cls.get(session, record_id)

    @classmethod
    async def delete(cls, session: AsyncSession, record_id: int):
        await session.execute(delete(cls.model).where(cls.model.id == record_id))
        await session.commit()


def CrudFactory(
        model: SQLModel,
        update_schema: Type[Schema],
        create_schema: Type[Schema],
        get_schema: Type[Schema],
) -> AbstractRepo:
    repo = type(
        "AbstractRepo",
        (AbstractRepo,),
        {
            "model": model,
            "update_schema": update_schema,
            "create_schema": create_schema,
            "get_schema": get_schema,
        }
    )
    return repo  # type: ignore
