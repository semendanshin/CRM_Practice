from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from config import config

from typing import AsyncGenerator

engine = create_async_engine(
    config.db_uri,
    echo=True,
)

sessionmaker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session
