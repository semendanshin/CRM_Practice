from .CrudFactory import CrudFactory
from db.models import SLA

from schemas.sla import SLACreate, SLAUpdate, SLAResponse


class SLARepo(
    CrudFactory(
        SLA,
        SLAUpdate,
        SLACreate,
        SLAResponse
    )
):
    pass
