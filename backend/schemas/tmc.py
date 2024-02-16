from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


"""
id: Mapped[int] = Column(Integer, primary_key=True)
name: Mapped[str] = Column(String)
description: Mapped[str] = Column(String)
created_at: Mapped[datetime] = Column(DateTime, default=datetime.now)
updated_at: Mapped[str] = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class TMCUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class TMCCreate(TMCUpdate):
    name: str
    description: str


class TMCResponse(TMCCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
