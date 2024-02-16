from __future__ import annotations

import datetime

from pydantic import BaseModel, ConfigDict
from typing import Optional


"""
id = Column(Integer, primary_key=True)
client_id = Column(Integer, ForeignKey('clients.id'))
client = relationship('Client')
token = Column(String, unique=True)
created_at = Column(DateTime, default=datetime.now)
"""


class BotAuthorizationUpdate(BaseModel):
    token: Optional[str] = None
    client_id: Optional[int] = None


class BotAuthorizationCreate(BotAuthorizationUpdate):
    token: str
    client_id: int


class BotAuthorizationResponse(BotAuthorizationCreate):
    model_config = ConfigDict(from_attributes=True)
