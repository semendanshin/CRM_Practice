from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
description: Mapped[str] = Column(String)
device_id: Mapped[int] = Column(Integer, ForeignKey('devices.id'))
from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
to_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
to_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
"""


# Update, Create, Response


class DeviceOperationMoveUpdate(BaseModel):
    description: Optional[str] = None
    device_id: Optional[int] = None
    from_warehouse_id: Optional[int] = None
    from_client_object_id: Optional[int] = None
    to_warehouse_id: Optional[int] = None
    to_client_object_id: Optional[int] = None


class DeviceOperationMoveCreate(DeviceOperationMoveUpdate):
    description: str
    device_id: int


class DeviceOperationMoveResponse(DeviceOperationMoveCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
