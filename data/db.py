import psycopg
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    host = os.getenv("DB_HOST")
    port=os.getenv("DB_PORT")
    dbname=os.getenv("DB_NAME")
    user=os.getenv("DB_USER")
    password=os.getenv("DB_PASSWORD")    

    DATABASE_URL = (
        f"postgresql+psycopg://{user}:{password}"
        f"@{host}:{port}/{dbname}"
    )
    engine = create_engine(DATABASE_URL)

    return engine