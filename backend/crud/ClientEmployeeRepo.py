from db.models import ClientEmployee
from .CrudFactory import CrudFactory
from schemas.client_employee import ClientEmployeeCreate, ClientEmployeeUpdate, ClientEmployeeResponse


class ClientEmployeeRepo(
    CrudFactory(
        ClientEmployee,
        ClientEmployeeUpdate,
        ClientEmployeeCreate,
        ClientEmployeeResponse,
    )
):
    pass
