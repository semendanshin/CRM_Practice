from .CrudFactory import CrudFactory
from db.models import InstructionAttachment

from schemas.instruction_attachment import InstructionAttachmentCreate, InstructionAttachmentUpdate, InstructionAttachmentResponse


class InstructionAttachmentRepo(
    CrudFactory(
        InstructionAttachment,
        InstructionAttachmentCreate,
        InstructionAttachmentUpdate,
        InstructionAttachmentResponse
    )
):
    pass
