from fastapi import APIRouter

from .auth.routes import router as auth_router
from .bot.routes import router as client_router
from .other.routes import router as other_router


router = APIRouter(
    prefix="",
    tags=[],
)

router.include_router(auth_router)
router.include_router(client_router)
router.include_router(other_router)
