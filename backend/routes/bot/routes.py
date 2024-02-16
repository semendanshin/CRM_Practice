from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from crud import TicketRepo
from .tokens import check_token, create_token
from db import get_session

from .exceptions import TokenEmptyException, TokenNotFoundException

from schemas.bot_authorization import BotAuthorizationResponse
from schemas.ticket import TicketResponse

router = APIRouter(
    prefix="/bot",
    tags=["bot"],
)


async def login_user(
        token: str,
        session: AsyncSession = Depends(get_session)
) -> BotAuthorizationResponse:
    try:
        client = await check_token(
            token,
            session,
        )
        return BotAuthorizationResponse(
            token=token,
            client_id=client.id,
        )
    except TokenEmptyException:
        raise HTTPException(status_code=400, detail="Token is empty")
    except TokenNotFoundException:
        raise HTTPException(status_code=404, detail="Token not found")


@router.post("/token")
async def token(
        client_id: int,
        session: AsyncSession = Depends(get_session),
):
    generated_token = await create_token(
        client_id,
        session,
    )

    return generated_token.token


@router.get("/tickets", response_model=list[TicketResponse])
async def get_tickets(
        client_id: BotAuthorizationResponse = Depends(login_user),
        session: AsyncSession = Depends(get_session),
):
    res = await TicketRepo.get_by_client_id(
        session,
        client_id.client_id,
    )
    return res


@router.post("/ticket")
async def create_ticket(
        client_id: BotAuthorizationResponse = Depends(login_user),
        session: AsyncSession = Depends(get_session),
):
    ticket = await TicketRepo.create(
        session,
        client_id.client_id,
    )
    return TicketResponse.model_validate(ticket)
