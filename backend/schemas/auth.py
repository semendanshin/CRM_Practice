from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

"""

class Authorization(Base):
    __tablename__ = 'authorizations'

    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    expired_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

"""


class AuthorizationUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    access_token: Optional[str]
    refresh_token: Optional[str]
    user_id: Optional[int]


class AuthorizationCreate(AuthorizationUpdate):
    access_token: str
    refresh_token: str
    user_id: int


class AuthorizationResponse(AuthorizationCreate):
    created_at: datetime
    expired_at: datetime
