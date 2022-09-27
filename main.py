import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.requests import Request
from starlette.responses import Response
from core.db import SessionLocal
from routes import routes
from user.models import User

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello"}


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)
