from .CrudFactory import CrudFactory
from db.models import TicketTaskStatus

from schemas.ticket_task_status import TicketTaskStatusCreate, TicketTaskStatusUpdate, TicketTaskStatusResponse


class TicketTaskStatusRepo(
    CrudFactory(
        TicketTaskStatus,
        TicketTaskStatusUpdate,
        TicketTaskStatusCreate,
        TicketTaskStatusResponse
    )
):
    pass
