from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id = Column(Integer, primary_key=True)
name = Column(String)
surname = Column(String)
patronymic = Column(String)
phone = Column(String)
email = Column(String)
position_id = Column(ForeignKey('positions.id'))
group_id = Column(Integer, ForeignKey('groups.id'))
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class EmployeeUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    position_id: Optional[int]
    group_id: Optional[int]


class EmployeeCreate(EmployeeUpdate):
    name: str
    surname: str
    patronymic: Optional[str]
    phone: str
    email: str
    position_id: int
    group_id: int


class EmployeeResponse(EmployeeCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
