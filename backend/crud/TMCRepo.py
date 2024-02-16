from .CrudFactory import CrudFactory
from db.models import TMC

from schemas.tmc import TMCCreate, TMCUpdate, TMCResponse


class TMCRepo(
    CrudFactory(
        TMC,
        TMCUpdate,
        TMCCreate,
        TMCResponse
    )
):
    pass
