from .CrudFactory import CrudFactory
from db.models import Position

from schemas.position import PositionCreate, PositionUpdate, PositionResponse


class PositionRepo(
    CrudFactory(
        Position,
        PositionUpdate,
        PositionCreate,
        PositionResponse
    )
):
    pass
