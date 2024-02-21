from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name = Column(String)
sla_id = Column(Integer, ForeignKey('slas.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class ClientTypeUpdate(BaseModel):
    name: Optional[str] = None
    sla_id: Optional[int] = None


class ClientTypeCreate(ClientTypeUpdate):
    name: str
    sla_id: int


class ClientTypeResponse(ClientTypeCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
