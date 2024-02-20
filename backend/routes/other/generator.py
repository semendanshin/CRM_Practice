from typing import Annotated, Type, Any, Coroutine

from fastapi import APIRouter, Depends, HTTPException
from db import get_session

from crud.CrudFactory import AbstractRepo
from routes.auth.routes import check_tokens_route
from schemas import EmployeeResponse
from pydantic import BaseModel, Field
from typing import Callable, Awaitable, Optional, Literal


class CustomHandler(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE"]
    handler: Callable[..., Coroutine[Any, Any, Any]]


class GeneratorParams(BaseModel):
    prefix: str
    repository: Type[AbstractRepo]
    custom_handlers: Optional[list[CustomHandler]] = Field(default_factory=list)
    get: bool = True
    get_all: bool = True
    post: bool = True
    put: bool = True
    delete: bool = True


def generate_crud_router(
        settings: GeneratorParams,
) -> APIRouter:

    if settings.custom_handlers is None:
        custom_handlers = []

    router = APIRouter(
        prefix=f"/{settings.prefix}",
        tags=[settings.prefix],
    )

    if settings.get_all:
        @router.get("/", response_model=list[settings.repository.get_schema])
        async def get_all(
                offset: int = 0,
                limit: int = 10,
                session=Depends(get_session),
                employee: EmployeeResponse = Depends(check_tokens_route),
        ):
            return await settings.repository.get_all(session, offset=offset, limit=limit)

    if settings.get:
        @router.get("/<record_id: int>", response_model=settings.repository.get_schema)
        async def get(
                record_id: int,
                session=Depends(get_session),
                employee: EmployeeResponse = Depends(check_tokens_route),
        ):
            obj = await settings.repository.get(session, record_id)
            if obj is None:
                raise HTTPException(status_code=404, detail=f"{settings.prefix.capitalize()} not found")
            return obj

    if settings.post:
        @router.post("", response_model=settings.repository.get_schema)
        async def create(
                data: Annotated[settings.repository.create_schema, Depends()],
                session=Depends(get_session),
                employee: EmployeeResponse = Depends(check_tokens_route),
        ):
            return await settings.repository.create(session, **data.model_dump())

    if settings.put:
        @router.put("/<record_id>", response_model=settings.repository.get_schema)
        async def update(
                record_id: int,
                data: Annotated[settings.repository.update_schema, Depends()],
                session=Depends(get_session),
                employee: EmployeeResponse = Depends(check_tokens_route),
        ):
            update_data = {key: value for key, value in data.model_dump().items() if value is not None}
            return await settings.repository.update(session, record_id, **update_data)

    if settings.delete:
        @router.delete("/<record_id>")
        async def delete(
                record_id: int,
                session=Depends(get_session),
                employee: EmployeeResponse = Depends(check_tokens_route),
        ):
            return await settings.repository.delete(session, record_id)

    for handler in settings.custom_handlers:
        method = handler.method.lower()
        if method == "get":
            router.get(f"/{handler.handler.__name__}")(handler.handler)
        elif method == "post":
            router.post(f"/{handler.handler.__name__}")(handler.handler)
        elif method == "put":
            router.put(f"/{handler.handler.__name__}")(handler.handler)
        elif method == "delete":
            router.delete(f"/{handler.handler.__name__}")(handler.handler)

    return router
