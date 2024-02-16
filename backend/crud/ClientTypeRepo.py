from .CrudFactory import CrudFactory
from db.models import ClientType

from schemas.client_type import ClientTypeUpdate, ClientTypeCreate, ClientTypeResponse


class ClientTypeRepo(
    CrudFactory(
        ClientType,
        ClientTypeUpdate,
        ClientTypeCreate,
        ClientTypeResponse
    )
):
    pass
