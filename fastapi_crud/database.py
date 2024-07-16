# database.py

from databases import Database
from os import environ
from dotenv.main import load_dotenv
from sqlalchemy import create_engine, MetaData

# .env variables
load_dotenv()

# DB connection
DB_CONN_URL = '{}://{}:{}@{}:{}/{}'.format(
    environ['DB_TYPE'],
    environ['DB_USER'],
    environ['DB_PASSWD'],
    environ['DB_HOST'],
    environ['DB_PORT'],
    environ['DB_NAME'],
)

db_instance = Database(
    DB_CONN_URL, 
    min_size=5,			
    max_size=1000,		
    pool_recycle=500	
    )

db_engine = create_engine(DB_CONN_URL)
db_metadata = MetaData()