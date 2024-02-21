from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id: Mapped[int] = Column(Integer, primary_key=True)
tmc_id: Mapped[int] = Column(Integer, ForeignKey('tmc.id'))
warehouse_id: Mapped[int] = Column(Integer, ForeignKey('warehouses.id'))
amount: Mapped[int] = Column(Integer)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TMCOperationInUpdate(BaseModel):
    tmc_id: Optional[int]
    warehouse_id: Optional[int]
    amount: Optional[int]


class TMCOperationInCreate(TMCOperationInUpdate):
    tmc_id: int
    warehouse_id: int
    amount: int


class TMCOperationInResponse(TMCOperationInCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime
