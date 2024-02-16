from pydantic import BaseModel, ConfigDict
from typing import Optional
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


class ClientObjectUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    client_id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    updated_at: Optional[datetime] = None


class ClientObjectCreate(ClientObjectUpdate):
    name: str
    client_id: int
    latitude: float
    longitude: float


class ClientObjectResponse(ClientObjectCreate):
    id: int
