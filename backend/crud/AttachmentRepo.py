from db.models import Attachment
from .CrudFactory import CrudFactory

from schemas.attachment import AttachmentCreate, AttachmentUpdate, AttachmentResponse


class AttachmentRepo(
    CrudFactory(
        Attachment,
        AttachmentUpdate,
        AttachmentCreate,
        AttachmentResponse
    )
):
    pass
