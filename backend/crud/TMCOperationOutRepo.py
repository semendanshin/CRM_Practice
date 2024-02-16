from .CrudFactory import CrudFactory
from db.models import TMCOperationOut

from schemas.tmc_operation_out import TMCOperationOutCreate, TMCOperationOutUpdate, TMCOperationOutResponse


class TMCOperationOutRepo(
    CrudFactory(
        TMCOperationOut,
        TMCOperationOutUpdate,
        TMCOperationOutCreate,
        TMCOperationOutResponse
    )
):
    pass
