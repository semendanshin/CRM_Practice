from .AbstractRepo import AbstractRepo
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Authorization


class AuthRepo(AbstractRepo):
    model = Authorization

    @classmethod
    async def get_by_refresh(self, session: AsyncSession, refresh: str):
        res = await session.execute(select(self.model).where(self.model.refresh == refresh))
        return res.scalar().first()
