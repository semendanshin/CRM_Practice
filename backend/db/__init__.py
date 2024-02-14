from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from config import config

from typing import AsyncGenerator

engine = create_async_engine(
    config.db_uri,
    echo=True,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session
