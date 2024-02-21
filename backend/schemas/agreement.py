"""
id = Column(Integer, primary_key=True)
    file_id = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
"""

from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import datetime
from typing import Optional


class AgreementUpdate(BaseModel):
    file_id: Optional[str] = Field(None)


class AgreementCreate(AgreementUpdate):
    file_id: str


class AgreementResponse(AgreementCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
