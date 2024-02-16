from .CrudFactory import CrudFactory
from db.models import Observer

from schemas.observer import ObserverCreate, ObserverUpdate, ObserverResponse


class ObserverRepo(
    CrudFactory(
        Observer,
        ObserverCreate,
        ObserverUpdate,
        ObserverResponse
    )
):
    pass
