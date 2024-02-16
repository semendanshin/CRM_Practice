from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from db import get_session

from crud.CrudFactory import AbstractRepo


def generate_crud_router(
        prefix: str,
        repository: AbstractRepo,
) -> APIRouter:

    router = APIRouter(
        prefix=f"/{prefix}",
        tags=[prefix],
    )

    @router.get("/", response_model=list[repository.get_schema])
    async def get_all(
            offset: int = 0,
            limit: int = 10,
            session=Depends(get_session),
    ):
        return await repository.get_all(session, offset, limit)

    @router.get("/<record_id: int>", response_model=repository.get_schema)
    async def get(
            record_id: int,
            session=Depends(get_session)
    ):
        obj = await repository.get(session, record_id)
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{prefix.capitalize()} not found")
        return obj

    @router.post("", response_model=repository.get_schema)
    async def create(
            data: Annotated[repository.create_schema, Depends()],
            session=Depends(get_session)
    ):
        return await repository.create(session, **data.model_dump())

    @router.put("/<record_id>", response_model=repository.get_schema)
    async def update(
            record_id: int,
            data: Annotated[repository.update_schema, Depends()],
            session=Depends(get_session)
    ):
        return await repository.update(session, record_id, **data.model_dump())

    @router.delete("/<record_id>")
    async def delete(
            record_id: int,
            session=Depends(get_session)
    ):
        return await repository.delete(session, record_id)

    return router
