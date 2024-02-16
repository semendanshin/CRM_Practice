from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
name: Mapped[str] = Column(String)
surname: Mapped[str] = Column(String)
patronymic: Mapped[str] = Column(String)
phone: Mapped[str] = Column(String)
email: Mapped[str] = Column(String)
client_id: Mapped[int] = Column(Integer, ForeignKey('clients.id'))
is_contact: Mapped[bool] = Column(Boolean)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class ClientEmployeeUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    client_id: Optional[int] = None
    is_contact: Optional[bool] = None


class ClientEmployeeCreate(ClientEmployeeUpdate):
    name: str
    surname: str
    patronymic: Optional[str]
    phone: str
    email: str
    client_id: int
    is_contact: bool


class ClientEmployeeResponse(ClientEmployeeCreate):
    id: int
    created_at: datetime
    updated_at: datetime
