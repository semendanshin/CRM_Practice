from .CrudFactory import CrudFactory
from db.models import Service

from schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse


class ServiceRepo(
    CrudFactory(
        Service,
        ServiceUpdate,
        ServiceCreate,
        ServiceResponse
    )
):
    pass
