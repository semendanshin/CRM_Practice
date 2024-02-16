from .CrudFactory import CrudFactory
from db.models import ClientPaymentStatus
from schemas.client_payment_status import ClientPaymentStatusUpdate, ClientPaymentStatusCreate, \
    ClientPaymentStatusResponse


class ClientPaymentStatusRepo(
    CrudFactory(
        ClientPaymentStatus,
        ClientPaymentStatusCreate,
        ClientPaymentStatusUpdate,
        ClientPaymentStatusResponse
    )
):
    pass
