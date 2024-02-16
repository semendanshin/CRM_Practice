from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name = Column(String)
client_object_id = Column(Integer, ForeignKey('client_objects.id'))
warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    client_object_id: Optional[int] = None
    warehouse_id: Optional[int] = None


class DeviceCreate(DeviceUpdate):
    name: str
    client_object_id: int
    warehouse_id: int


class DeviceResponse(DeviceCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
