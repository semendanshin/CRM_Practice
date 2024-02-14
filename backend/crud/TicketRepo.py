from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Ticket
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(Ticket)):
    @classmethod
    async def get_ticket_by_id(cls, session: AsyncSession, record_id: int) -> "Ticket":
        res = await session.execute(select(cls.Ticket).where(Ticket.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_ticket_by_employee_id(cls, session: AsyncSession, record_id: int) -> "Ticket":
        res = await session.execute(select(cls.Ticket).where(Ticket.employee_id == record_id))
        return res.all()

    @classmethod
    async def get_all_tickets(cls, session: AsyncSession) -> "Ticket":
        res = await session.execute(select(cls.Ticket))
        return res.all()

    @classmethod
    async def create_ticket(cls, session: AsyncSession, **kwargs) -> "Ticket":
        instance = cls.Ticket(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_ticket(cls, session: AsyncSession, ticket_id: int):
        res = await session.execute(select(Ticket).where(Ticket.id == ticket_id))
        client_payment_status_to_delete = res.scalar_one()
        await session.delete(client_payment_status_to_delete)
        await session.commit()
