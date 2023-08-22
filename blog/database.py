from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# create database engine 
engin = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


# create session
SessionLocal = sessionmaker(bind=engin, autocommit=False, autoflush=False)


# declare mapping
Base = declarative_base()