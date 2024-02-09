from sqlalchemy.ext.asyncio import create_async_engine
from config import config

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

engine = create_async_engine(
    config.DB_URI.get_secret_value(),
    echo=True,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session
