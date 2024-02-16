from .CrudFactory import CrudFactory
from db.models import ServiceToTicket

from schemas.service_to_ticket import ServiceToTicketCreate, ServiceToTicketUpdate, ServiceToTicketResponse


class ServiceToTicketRepo(
    CrudFactory(
        ServiceToTicket,
        ServiceToTicketUpdate,
        ServiceToTicketCreate,
        ServiceToTicketResponse
    )
):
    pass
