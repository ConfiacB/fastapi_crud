# router.py

from databases.core import Database
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from fastapi.requests import Request
from typing import List

# Memo schema
from fastapi_crud.memo.schema import MemoCreate
from fastapi_crud.memo.schema import MemoSelect
# Memo model
from fastapi_crud.memo.model import memo

memo_router = APIRouter()

def get_db_conn(request: Request):
    return request.state.db_conn		# db_conn from middleware

# create memo
@memo_router.post("/memo")
async def memo_create(
    req: MemoCreate,					
    db: Database = Depends(get_db_conn)
    ):
    
    query = memo.insert()				# (feat.sqlalchemy)
    values = req
    await db.execute(query, values)		# (feat.databases)
    
    return {**req.dict()}

@memo_router.get("/memo/find/{idx}", response_model=MemoSelect)
async def memo_findone(
    idx: int,
    db: Database = Depends(get_db_conn)
):
    query = memo.select().where(memo.columns.idx == idx)
    return await db.fetch_one(query)

@memo_router.get("/memo/list/{page}", response_model=List[MemoSelect])
async def memo_findone(
    page: int = 1,
    limit: int = 10,
    db: Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = memo.select().offset(offset).limit(limit)
    return await db.fetch_all(query)

@memo_router.delete("/memo/{idx}")
async def memo_findone(
    idx: int,
    db: Database = Depends(get_db_conn)
):
    query = memo.delete().where(memo.columns.idx == idx)
    await db.execute(query)
    return {"result": "success"}