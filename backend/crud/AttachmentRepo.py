from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Attachment
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Attachment)):
    @classmethod
    async def get_attachment_by_id(cls, session: AsyncSession, record_id: int) -> "Attachment":
        res = await session.execute(select(cls.Attachment).where(Attachment.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_attachments(cls, session: AsyncSession) -> "Attachment":
        res = await session.execute(select(cls.Attachment))
        return res.scalar().all()

    @classmethod
    async def create_attachment(cls, session: AsyncSession, **kwargs) -> "Attachment":
        instance = cls.Attachment(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_attachment(cls, session: AsyncSession, attachment_id: int):
        res = await session.execute(select(Attachment).where(Attachment.id == attachment_id))
        attachment_to_delete = res.scalar_one()
        await session.delete(attachment_to_delete)
        await session.commit()
