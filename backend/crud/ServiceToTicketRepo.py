from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import ServiceToTicket
import CrudFactory


class ClientRepo(CrudFactory.CrudFactory(ServiceToTicket)):
    @classmethod
    async def get_service_to_ticket_by_id(cls, session: AsyncSession, record_id: int) -> "ServiceToTicket":
        res = await session.execute(select(cls.ServiceToTicket).where(ServiceToTicket.id == record_id))
        return res.scalar().first()

    @classmethod
    async def get_all_service_to_tickets(cls, session: AsyncSession) -> "ServiceToTicket":
        res = await session.execute(select(cls.ServiceToTicket))
        return res.scalar().all()

    @classmethod
    async def create_service_to_ticket(cls, session: AsyncSession, **kwargs) -> "ServiceToTicket":
        instance = cls.ServiceToTicket(**kwargs)
        session.add(instance)
        await session.commit()
        return instance

    @classmethod
    async def delete_service_to_ticket(cls, session: AsyncSession, service_to_ticket_id: int):
        res = await session.execute(select(ServiceToTicket).where(ServiceToTicket.id == service_to_ticket_id))
        service_to_ticket_to_delete = res.scalar_one()
        await session.delete(service_to_ticket_to_delete)
        await session.commit()
