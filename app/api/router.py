from fastapi import APIRouter
from app.api.endpoints import users

router = APIRouter()

# Include endpoint routers
router.include_router(users.router, prefix="/users")
#router.include_router(devices.router, prefix="/devices")

# Export the main router
__all__ = ["router"]
