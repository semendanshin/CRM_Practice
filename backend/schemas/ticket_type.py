from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name = Column(String)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TicketTypeUpdate(BaseModel):
    name: Optional[str] = None


class TicketTypeCreate(TicketTypeUpdate):
    name: str


class TicketTypeResponse(TicketTypeCreate):
    model_config = ConfigDict()
    id: int
    created_at: datetime
    updated_at: datetime