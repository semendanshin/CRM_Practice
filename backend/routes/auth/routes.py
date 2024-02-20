from typing import Annotated

from fastapi import Depends, HTTPException, Cookie, Response
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from config import config
from db import get_session
from routes.auth.exceptions import TokenEmptyException, TokenNotFoundException, TokenInvalidException, \
    TokenExpiredException
from routes.auth.tokens import create_tokens, check_token, refresh_tokens, Tokens

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


def update_tokens_in_cookies(response: Response, tokens: Tokens):
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")

    response.set_cookie(key="access_token", value=tokens.access_token, expires=config.ACCESS_EXPIRE_DAYS * 24 * 60 * 60)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, expires=config.REFRESH_EXPIRE_DAYS * 24 * 60 * 60)


def jwt_cookie_wrapper(
        access_token: Annotated[str, Cookie(default="")],
        refresh_token: Annotated[str, Cookie(default="")],
):
    return Tokens(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.post("/create")
async def create_tokens_route(
        employee_id: int,
        response: Response,
        session: AsyncSession = Depends(get_session),
):
    tokens = await create_tokens(
        session,
        employee_id,
    )

    update_tokens_in_cookies(response, tokens)

    return tokens


@router.post("/check")
async def check_tokens_route(
        tokens: Tokens = Depends(jwt_cookie_wrapper),
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
        response: Response,
        tokens: Tokens = Depends(jwt_cookie_wrapper),
        session: AsyncSession = Depends(get_session)
):
    try:
        tokens = await refresh_tokens(
            session,
            tokens
        )

        update_tokens_in_cookies(response, tokens)

        return tokens

    except TokenEmptyException:
        raise HTTPException(status_code=400, detail="Token is empty")
    except TokenNotFoundException:
        raise HTTPException(status_code=404, detail="Token not found")
    except TokenInvalidException:
        raise HTTPException(status_code=400, detail="Token is invalid")
    except TokenExpiredException:
        raise HTTPException(status_code=400, detail="Token is expired")
