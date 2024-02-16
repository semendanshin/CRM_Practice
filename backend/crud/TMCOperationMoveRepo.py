from .CrudFactory import CrudFactory
from db.models import TMCOperationMove

from schemas.tmc_operation_move import TMCOperationMoveCreate, TMCOperationMoveUpdate, TMCOperationMoveResponse


class TMCOperationMoveRepo(
    CrudFactory(
        TMCOperationMove,
        TMCOperationMoveUpdate,
        TMCOperationMoveCreate,
        TMCOperationMoveResponse
    )
):
    pass
