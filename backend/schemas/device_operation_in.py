from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id: Mapped[int] = Column(Integer, primary_key=True)
description: Mapped[str] = Column(String)
device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))
warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class DeviceOperationInUpdate(BaseModel):
    description: Optional[str] = None
    device_id: Optional[int] = None
    warehouse_id: Optional[int] = None


class DeviceOperationInCreate(DeviceOperationInUpdate):
    description: str
    device_id: int
    warehouse_id: int


class DeviceOperationInResponse(DeviceOperationInCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
