from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id: Mapped[int] = Column(Integer, primary_key=True)
    ticket_id: Mapped[int] = Column(Integer, ForeignKey('tickets.id'))
    employee_id: Mapped[int] = Column(Integer, ForeignKey('employees.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate
    =datetime.now)
"""


class ObserverUpdate(BaseModel):
    ticket_id: Optional[int] = None
    employee_id: Optional[int] = None


class ObserverCreate(ObserverUpdate):
    ticket_id: int
    employee_id: int


class ObserverResponse(ObserverCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
