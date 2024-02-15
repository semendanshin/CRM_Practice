from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import InstructionAttachment
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(InstructionAttachment)):
    @classmethod
    async def get_instruction_attachment_by_id(cls, session: AsyncSession, record_id: int) -> "InstructionAttachment":
        res = await session.execute(select(cls.InstructionAttachment).where(InstructionAttachment.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_instruction_attachments(cls, session: AsyncSession) -> "InstructionAttachment":
        res = await session.execute(select(cls.InstructionAttachment))
        return res.scalar().all()

    @classmethod
    async def create_instruction_attachment(cls, session: AsyncSession, **kwargs) -> "InstructionAttachment":
        instance = cls.InstructionAttachment(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_instruction_attachment(cls, session: AsyncSession, instruction_attachment_id: int):
        res = await session.execute(
            select(InstructionAttachment)
            .where(InstructionAttachment.id == instruction_attachment_id)
        )
        instruction_attachment_to_delete = res.scalar_one()
        await session.delete(instruction_attachment_to_delete)
        await session.commit()
