from fastapi import APIRouter

from apps.controller import user

api_v1_router = APIRouter()
api_v1_router.include_router(user.router, prefix="/user", tags=["user"])
