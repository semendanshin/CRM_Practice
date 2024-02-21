from .CrudFactory import CrudFactory
from db.models import TicketTask

from schemas.ticket_task import TicketTaskCreate, TicketTaskUpdate, TicketTaskResponse


class TicketTaskRepo(
    CrudFactory(
        TicketTask,
        TicketTaskUpdate,
        TicketTaskCreate,
        TicketTaskResponse
    )
):
    pass
