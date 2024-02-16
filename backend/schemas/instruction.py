from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
category = Column(String)
short_description = Column(String)
description = Column(String)
created_at = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""


class InstructionUpdate(BaseModel):
    category: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None


class InstructionCreate(InstructionUpdate):
    category: str
    short_description: str
    description: str


class InstructionResponse(InstructionCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
