from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings
#from psycopg.rows import dict_row
# import time
# import psycopg

SQLALCHEMY_DATABASE_URL =f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,  
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg.connect(host='localhost',dbname='fastapi',user='postgres',
#                            password='ISMAILali123',row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connection was succesfull 👌")
#         break
#     except Exception as error:
#         print("connect to database failed 😒")
#         print("Error: ", error)
#         time.sleep(3)

#while True its not important any more because we connect to db by sqlalchamy it just for docmuntation now search more about this 

