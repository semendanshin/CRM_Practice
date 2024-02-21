from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuthorizationUpdate(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None


class AuthorizationCreate(AuthorizationUpdate):
    employee_id: int
    access_token: str
    refresh_token: str


class AuthorizationResponse(AuthorizationCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
