from pydantic import BaseModel


class TicketCreate(BaseModel):
    token: str
    description: str


class TicketResponse(BaseModel):
    description: str
    status: str
    

