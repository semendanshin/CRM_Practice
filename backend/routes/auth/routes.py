from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from routes.auth.tokens import create_tokens, check_token, refresh_tokens, Tokens
from routes.auth.exceptions import TokenEmptyException, TokenNotFoundException, TokenInvalidException, \
    TokenExpiredException
from db import get_session

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/create")
async def create_tokens_route(
        employee_id: int,
        received_tokens: Tokens = None,
        session: AsyncSession = Depends(get_session)
):
    return await create_tokens(
        session,
        employee_id,
        received_tokens
    )


@router.post("/check")
async def check_tokens_route(
        tokens: Tokens,
        session: AsyncSession = Depends(get_session)
):
    try:
        return await check_token(
            session,
            tokens
        )
    except TokenEmptyException:
        raise HTTPException(status_code=400, detail="Token is empty")
    except TokenNotFoundException:
        raise HTTPException(status_code=404, detail="Token not found")
    except TokenInvalidException:
        raise HTTPException(status_code=400, detail="Token is invalid")
    except TokenExpiredException:
        raise HTTPException(status_code=400, detail="Token is expired")


@router.post("/refresh")
async def refresh_tokens_route(
        tokens: Tokens,
        session: AsyncSession = Depends(get_session)
):
    try:
        return refresh_tokens(
            session,
            tokens
        )
    except TokenEmptyException:
        raise HTTPException(status_code=400, detail="Token is empty")
    except TokenNotFoundException:
        raise HTTPException(status_code=404, detail="Token not found")
    except TokenInvalidException:
        raise HTTPException(status_code=400, detail="Token is invalid")
    except TokenExpiredException:
        raise HTTPException(status_code=400, detail="Token is expired")
