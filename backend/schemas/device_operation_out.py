from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
description: Mapped[str] = Column(String)
device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))

from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))

created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


# Update, Create, Response


class DeviceOperationOutUpdate(BaseModel):
    description: Optional[str]
    device_id: Optional[int]
    from_warehouse_id: Optional[int]
    from_client_object_id: Optional[int]
    updated_at: Optional[datetime]


class DeviceOperationOutCreate(DeviceOperationOutUpdate):
    description: str
    device_id: int
    from_warehouse_id: int
    from_client_object_id: int


class DeviceOperationOutResponse(DeviceOperationOutCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
