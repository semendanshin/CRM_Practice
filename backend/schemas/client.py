from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
name: Mapped[str] = Column(String)
type_id: Mapped[int] = Column(Integer, ForeignKey('client_types.id'))
agreement_id: Mapped[int] = Column(Integer, ForeignKey('agreements.id'))
manager_id = Column(Integer, ForeignKey('employees.id'))
monthly_payment = Column(Float)
comment = Column(String)
payment_status_id: Mapped[int] = Column(Integer, ForeignKey('client_payment_statuses.id'))

created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class ClientUpdate(BaseModel):
    name: Optional[str]
    type_id: Optional[int]
    agreement_id: Optional[int]
    manager_id: Optional[int]
    monthly_payment: Optional[float]
    comment: Optional[str]
    payment_status_id: Optional[int]


class ClientCreate(ClientUpdate):
    name: str
    type_id: int
    agreement_id: int
    manager_id: int
    monthly_payment: float
    comment: str
    payment_status_id: int


class ClientResponse(ClientCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
