from db.models import Devices
from .CrudFactory import CrudFactory

from schemas.device import DeviceCreate, DeviceUpdate, DeviceResponse


class DeviceRepo(
    CrudFactory(
        Devices,
        DeviceUpdate,
        DeviceCreate,
        DeviceResponse
    )
):
    pass
