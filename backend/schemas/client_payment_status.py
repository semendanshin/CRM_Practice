from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name = Column(String)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class ClientPaymentStatusUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str]


class ClientPaymentStatusCreate(ClientPaymentStatusUpdate):
    name: str


class ClientPaymentStatusResponse(ClientPaymentStatusCreate):
    id: int
    created_at: datetime
    updated_at: datetime
