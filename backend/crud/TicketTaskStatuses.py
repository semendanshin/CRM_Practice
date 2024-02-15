from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TicketTaskStatuses
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TicketTaskStatuses)):
    @classmethod
    async def get_ticket_task_status(cls, session: AsyncSession, record_id: int) -> "TicketTaskStatuses":
        res = await session.execute(select(cls.TicketTaskStatuses).where(TicketTaskStatuses.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_ticket_task_statuses(cls, session: AsyncSession) -> "TicketTaskStatuses":
        res = await session.execute(select(cls.TicketTaskStatuses))
        return res.scalar().all()

    @classmethod
    async def create_ticket_task_status(cls, session: AsyncSession, **kwargs) -> "TicketTaskStatuses":
        instance = cls.TicketTaskStatuses(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_ticket_task_status(cls, session: AsyncSession, ticket_task_statuses_id: int):
        res = await session.execute(select(TicketTaskStatuses).where(TicketTaskStatuses.id == ticket_task_statuses_id))
        client_payment_status_to_delete = res.scalar_one()
        await session.delete(client_payment_status_to_delete)
        await session.commit()
