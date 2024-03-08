from fastapi import APIRouter

from compiler_exploter.routes import compile

api_router = APIRouter()
api_router.include_router(compile.router, tags=["compile"])
