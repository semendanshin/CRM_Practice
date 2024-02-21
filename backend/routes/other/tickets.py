from db import get_session
from db.models import Ticket

from crud import TicketRepo
from routes.auth.routes import check_tokens_route
from schemas import TicketCreate, TicketResponse

from fastapi import APIRouter, Depends, HTTPException


async def get_employees_tickets(
        offset: int = 0,
        limit: int = 10,
        session=Depends(get_session),
        employee=Depends(check_tokens_route),
):
    return await TicketRepo.get_all(session, Ticket.employee_id == employee.id, offset=offset, limit=limit)
