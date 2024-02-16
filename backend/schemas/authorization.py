from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuthorizationUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    user_id: Optional[int] = None


class AuthorizationCreate(AuthorizationUpdate):
    access_token: str
    refresh_token: str
    user_id: int


class AuthorizationResponse(AuthorizationCreate):
    created_at: datetime
    expired_at: datetime