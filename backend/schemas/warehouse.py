from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name = Column(String)
client_id = Column(Integer, ForeignKey('clients.id'))
latitude = Column(Float)
longitude = Column(Float)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class WarehouseUpdate(BaseModel):
    name: Optional[str]
    client_id: Optional[int]
    latitude: Optional[float]
    longitude: Optional[float]


class WarehouseCreate(WarehouseUpdate):
    name: str
    client_id: int
    latitude: float
    longitude: float


class WarehouseResponse(WarehouseCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
