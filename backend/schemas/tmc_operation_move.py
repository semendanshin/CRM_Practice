from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id: Mapped[int] = Column(Integer, primary_key=True)
tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
to_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
to_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
amount: Mapped[int] = Column(Integer)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TMCOperationMoveUpdate(BaseModel):
    tmc_id: Optional[int] = None
    from_warehouse_id: Optional[int] = None
    from_client_object_id: Optional[int] = None
    to_warehouse_id: Optional[int] = None
    to_client_object_id: Optional[int] = None
    amount: Optional[int] = None


class TMCOperationMoveCreate(TMCOperationMoveUpdate):
    tmc_id: int
    amount: int


class TMCOperationMoveResponse(TMCOperationMoveCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
