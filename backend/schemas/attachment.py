"""
id = Column(Integer, primary_key=True)
    file_id = Column(String)
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AttachmentUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    file_id: Optional[str] = None
    ticket_id: Optional[int] = None


class AttachmentCreate(AttachmentUpdate):
    file_id: str
    ticket_id: int


class AttachmentResponse(AttachmentCreate):
    id: int
    created_at: datetime
    updated_at: datetime
