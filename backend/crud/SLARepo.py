from .CrudFactory import CrudFactory
from db.models import SLA

from schemas.sla import SLACreate, SLAUpdate, SLAResponse


class SLARepo(
    CrudFactory(
        SLA,
        SLACreate,
        SLAUpdate,
        SLAResponse
    )
):
    pass
