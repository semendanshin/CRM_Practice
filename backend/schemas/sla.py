from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

"""
id = Column(Integer, primary_key=True)
file_id = Column(String)
created_at = Column(DateTime, default=datetime.now)
"""


class SLAUpdate(BaseModel):
    file_id: Optional[str]


class SLACreate(SLAUpdate):
    file_id: str


class SLAResponse(SLACreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
