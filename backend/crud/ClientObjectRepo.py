from db.models import ClientObject
from .CrudFactory import CrudFactory

from schemas.client_object import ClientObjectCreate, ClientObjectUpdate, ClientObjectResponse


class ClientObjectRepo(
    CrudFactory(
        ClientObject,
        ClientObjectCreate,
        ClientObjectUpdate,
        ClientObjectResponse
    )
):
    pass
