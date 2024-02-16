from .CrudFactory import CrudFactory
from db.models import TMCOperationIn

from schemas.tmc_operation_in import TMCOperationInCreate, TMCOperationInUpdate, TMCOperationInResponse


class TMCOperationInRepo(
    CrudFactory(
        TMCOperationIn,
        TMCOperationInUpdate,
        TMCOperationInCreate,
        TMCOperationInResponse
    )
):
    pass
