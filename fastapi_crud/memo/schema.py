# schema.py

from datetime import datetime
from pydantic import BaseModel

# Pydantic Type Hinting
class MemoCreate(BaseModel):
    regdate : datetime
    title : str
    body : str

class MemoSelect(BaseModel):
    idx : int
    regdate : datetime
    title : str
    body : str