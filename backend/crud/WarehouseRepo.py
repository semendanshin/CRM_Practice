from .CrudFactory import CrudFactory
from db.models import Warehouse

from schemas.warehouse import WarehouseCreate, WarehouseUpdate, WarehouseResponse


class WarehouseRepo(
    CrudFactory(
        Warehouse,
        WarehouseUpdate,
        WarehouseCreate,
        WarehouseResponse
    )
):
    pass
