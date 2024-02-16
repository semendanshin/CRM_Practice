from db.models import Client
from .CrudFactory import CrudFactory

from schemas.client import ClientCreate, ClientUpdate, ClientResponse


class ClientRepo(
    CrudFactory(
        Client,
        ClientCreate,
        ClientUpdate,
        ClientResponse
    )
):
    pass
