from .CrudFactory import CrudFactory
from db.models import Instruction

from schemas.instruction import InstructionCreate, InstructionUpdate, InstructionResponse


class InstructionRepo(
    CrudFactory(
        Instruction,
        InstructionCreate,
        InstructionUpdate,
        InstructionResponse
    )
):
    pass
