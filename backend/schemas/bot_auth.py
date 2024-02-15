from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator

from db.models import TicketStatus


class BotAuthorizationResponse(BaseModel):
    client_id: int


class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    description: str
    status: str

    @field_validator("status", mode="before")
    def check_status(cls, v):
        if isinstance(v, TicketStatus):
            return v.name
