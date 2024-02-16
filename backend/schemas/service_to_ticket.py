from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
service_id: Mapped[int] = Column(Integer, ForeignKey('services.id'))
ticket_id: Mapped[int] = Column(Integer, ForeignKey('tickets.id'))
amount: Mapped[int] = Column(Integer)
price: Mapped[float] = Column(Float)
unit: Mapped[str] = Column(String)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class ServiceToTicketUpdate(BaseModel):
    service_id: Optional[int] = None
    amount: Optional[int] = None
    price: Optional[float] = None
    unit: Optional[str] = None


class ServiceToTicketCreate(ServiceToTicketUpdate):
    ticket_id: int
    service_id: int
    amount: int
    price: float
    unit: str


class ServiceToTicketResponse(ServiceToTicketCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
