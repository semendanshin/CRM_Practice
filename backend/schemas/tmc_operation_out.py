from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id: Mapped[int] = Column(Integer, primary_key=True)
tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
amount: Mapped[int] = Column(Integer)
from_warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
from_client_object_id: Mapped[int] = Column(Integer, ForeignKey('client_objects.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TMCOperationOutUpdate(BaseModel):
    amount: Optional[int]
    from_warehouse_id: Optional[int]
    from_client_object_id: Optional[int]


class TMCOperationOutCreate(TMCOperationOutUpdate):
    tmc_id: int
    amount: int
    from_warehouse_id: int
    from_client_object_id: int


class TMCOperationOutResponse(TMCOperationOutCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
