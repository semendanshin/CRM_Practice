from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .CrudFactory import CrudFactory
from db.models import Ticket

from schemas.ticket import TicketCreate, TicketUpdate, TicketResponse


class TicketRepo(
    CrudFactory(
        Ticket,
        TicketUpdate,
        TicketCreate,
        TicketResponse
    )
):
    @classmethod
    async def get_by_client_id(cls, session: AsyncSession, client_id: int) -> Sequence[TicketResponse]:
        if not isinstance(client_id, int):
            raise TypeError("client_id must be an integer")
        res = await session.execute(
            select(cls.model).where(cls.model.client_id == client_id)
        )
        objects = res.scalars().all()
        return [cls.get_schema.model_validate(obj) for obj in objects]
