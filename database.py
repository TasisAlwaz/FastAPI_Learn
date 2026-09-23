from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:postgres@localhost:5432/Telusko"
engine = create_engine(db_url )
session = sessionmaker(
    autocommit = False,
    autoflush= False, 
    bind = engine
    )
