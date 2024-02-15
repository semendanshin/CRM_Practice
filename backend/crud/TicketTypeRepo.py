from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import TicketType
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(TicketType)):
    @classmethod
    async def get_ticket_type_by_id(cls, session: AsyncSession, record_id: int) -> "TicketType":
        res = await session.execute(select(cls.TicketType).where(TicketType.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_ticket_types(cls, session: AsyncSession) -> "TicketType":
        res = await session.execute(select(cls.TicketType))
        return res.scalar().all()

    @classmethod
    async def create_ticket_task_status(cls, session: AsyncSession, **kwargs) -> "TicketType":
        instance = cls.TicketType(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_ticket_type(cls, session: AsyncSession, ticket_type_id: int):
        res = await session.execute(select(TicketType).where(TicketType.id == ticket_type_id))
        client_payment_status_to_delete = res.scalar_one()
        await session.delete(client_payment_status_to_delete)
        await session.commit()
