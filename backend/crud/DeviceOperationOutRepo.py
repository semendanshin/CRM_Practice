from .CrudFactory import CrudFactory
from db.models import DeviceOperationOut

from schemas.device_operation_out import DeviceOperationOutCreate, DeviceOperationOutUpdate, DeviceOperationOutResponse


class DeviceOperationOutRepo(
    CrudFactory(
        DeviceOperationOut,
        DeviceOperationOutCreate,
        DeviceOperationOutUpdate,
        DeviceOperationOutResponse,
    )
):
    pass
