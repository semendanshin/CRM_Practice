from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
file_id = Column(String)
instruction_id = Column(Integer, ForeignKey('instructions.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class InstructionAttachmentUpdate(BaseModel):
    file_id: Optional[str] = None
    instruction_id: Optional[int] = None


class InstructionAttachmentCreate(InstructionAttachmentUpdate):
    file_id: str
    instruction_id: int


class InstructionAttachmentResponse(InstructionAttachmentCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
