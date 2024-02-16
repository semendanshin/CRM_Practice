from .CrudFactory import CrudFactory
from db.models import DevicesOperationIn

from schemas.device_operation_in import DeviceOperationInCreate, DeviceOperationInUpdate, DeviceOperationInResponse


class DeviceOperationInRepo(
    CrudFactory(
        DevicesOperationIn,
        DeviceOperationInUpdate,
        DeviceOperationInCreate,
        DeviceOperationInResponse
    )
):
    pass
