from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
name
updated_at
created_at
"""


class PositionUpdate(BaseModel):
    name: Optional[str] = None


class PositionCreate(PositionUpdate):
    name: str


class PositionResponse(PositionUpdate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    updated_at: datetime
    created_at: datetime
