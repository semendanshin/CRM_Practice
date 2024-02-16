from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
description = Column(String)
status_id = Column(Integer, ForeignKey('ticket_statuses.id'))
type_id = Column(Integer, ForeignKey('ticket_types.id'))
client_id = Column(Integer, ForeignKey('clients.id'))
employee_id = Column(Integer, ForeignKey('employees.id'))
hours_spent = Column(Float)
client_agreement_id = Column(Integer, ForeignKey('client_agreements.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TicketUpdate(BaseModel):
    description: Optional[str] = None
    status_id: Optional[int] = None
    type_id: Optional[int] = None
    client_id: Optional[int] = None
    employee_id: Optional[int] = None
    hours_spent: Optional[float] = None
    client_agreement_id: Optional[int] = None


class TicketCreate(TicketUpdate):
    description: str
    status_id: int
    type_id: int
    client_id: int
    employee_id: int
    client_agreement_id: int


class TicketResponse(TicketCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
