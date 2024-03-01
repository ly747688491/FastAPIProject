from fastapi import APIRouter

from apps.controller import user, demo

api_v1_router = APIRouter()
api_v1_router.include_router(user.router, prefix="/user", tags=["user"])
api_v1_router.include_router(demo.router, prefix="/demo", tags=["demo"])
