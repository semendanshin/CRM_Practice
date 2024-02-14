from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TicketTask
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TicketTask)):
    @classmethod
    async def get_ticket_task(cls, session: AsyncSession, record_id: int) -> "TicketTask":
        res = await session.execute(select(cls.TicketTask).where(TicketTask.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_ticket_tasks(cls, session: AsyncSession) -> "TicketTask":
        res = await session.execute(select(cls.TicketTask))
        return res.scalar().all()

    @classmethod
    async def create_ticket_task(cls, session: AsyncSession, **kwargs) -> "TicketTask":
        instance = cls.TicketTask(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_ticket_task(cls, session: AsyncSession, ticket_task_id: int):
        res = await session.execute(select(TicketTask).where(TicketTask.id == ticket_task_id))
        client_payment_status_to_delete = res.scalar_one()
        await session.delete(client_payment_status_to_delete)
        await session.commit()
