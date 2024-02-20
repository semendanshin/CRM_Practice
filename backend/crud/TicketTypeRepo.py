from sqlalchemy import select

from .CrudFactory import CrudFactory
from db.models import TicketType

from schemas.ticket_type import TicketTypeCreate, TicketTypeUpdate, TicketTypeResponse


class TicketTypeRepo(
    CrudFactory(
        TicketType,
        TicketTypeUpdate,
        TicketTypeCreate,
        TicketTypeResponse
    )
):
    @classmethod
    async def get_by_name(cls, session, name: str):
        res = await session.execute(
            select(cls.model).filter_by(name=name)
        )
        obj = res.scalar_one()
        return cls.get_schema.model_validate(obj) if obj else None
