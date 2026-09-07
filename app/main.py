from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.items import router as items_router
from app.api.math import router as math_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)
app.include_router(health_router)
app.include_router(items_router)
app.include_router(math_router)
