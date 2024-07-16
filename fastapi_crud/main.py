# main.py

from fastapi import FastAPI, Request
from fastapi_crud.database import db_instance
from fastapi_crud.memo.router import memo_router

app = FastAPI(
    title="Memo API",
    description="Memo CRUD API project",
    version="0.0.1"
)

# when server start, db connect
@app.on_event("startup")
async def startup():
    await db_instance.connect()

# at the end, db disconnect
@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()

# fastapi middleware
@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(memo_router)