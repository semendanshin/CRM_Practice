from .CrudFactory import CrudFactory
from db.models import TicketType

from schemas.ticket_type import TicketTypeCreate, TicketTypeUpdate, TicketTypeResponse


class TicketTypeRepo(
    CrudFactory(
        TicketType,
        TicketTypeCreate,
        TicketTypeUpdate,
        TicketTypeResponse
    )
):
    pass
