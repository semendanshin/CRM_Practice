from .CrudFactory import CrudFactory
from db.models import DeviceOperationMove

from schemas.device_operation_move import DeviceOperationMoveCreate, DeviceOperationMoveUpdate, DeviceOperationMoveResponse


class DeviceOperationMoveRepo(
    CrudFactory(
        DeviceOperationMove,
        DeviceOperationMoveUpdate,
        DeviceOperationMoveCreate,
        DeviceOperationMoveResponse
    )
):
    pass
