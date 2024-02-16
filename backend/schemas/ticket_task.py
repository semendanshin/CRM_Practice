from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id = Column(Integer, primary_key=True)
description = Column(String)
status_id = Column(Integer, ForeignKey('ticket_task_statuses.id'))
ticket_id = Column(Integer, ForeignKey('tickets.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TicketTaskUpdate(BaseModel):
    id: int
    description: Optional[str] = None
    status_id: Optional[int] = None
    ticket_id: Optional[int] = None


class TicketTaskCreate(BaseModel):
    description: str
    status_id: int
    ticket_id: int


class TicketTaskResponse(TicketTaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
