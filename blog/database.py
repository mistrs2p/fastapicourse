from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
# SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:mistrs2P@localhost:3306/mydbuse'

# create database engine
engin = create_engine(SQLALCHEMY_DATABASE_URL)


# create session
SessionLocal = sessionmaker(bind=engin, autocommit=False, autoflush=False)


# declare mapping
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
