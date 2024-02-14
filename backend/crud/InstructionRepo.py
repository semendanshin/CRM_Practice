from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Instruction
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Instruction)):
    @classmethod
    async def get_instruction_by_id(cls, session: AsyncSession, record_id: int) -> "Instruction":
        res = await session.execute(select(cls.Instruction).where(Instruction.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_instructions(cls, session: AsyncSession) -> "Instruction":
        res = await session.execute(select(cls.Instruction))
        return res.scalar().all()

    @classmethod
    async def create_instruction(cls, session: AsyncSession, **kwargs) -> "Instruction":
        instance = cls.Instruction(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_instruction(cls, session: AsyncSession, instruction_id: int):
        res = await session.execute(select(Instruction).where(Instruction.id == instruction_id))
        instruction_to_delete = res.scalar_one()
        await session.delete(instruction_to_delete)
        await session.commit()
