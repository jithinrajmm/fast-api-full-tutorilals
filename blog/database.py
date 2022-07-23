from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# connecting to the data base
# This part is used to connect the database
# ./fast_api.db is the name of the database file which created under the same directory

SQLALCHEMY_DATABASE_URL = "sqlite:///./fast_api.db"

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# creating alchemy engine, later we are going to use the engines 
# connect_args={"check_same_thread": False ->This argument only needed for the sqlite , no need of other databases
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# each session is the instace for the database session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# this declarative_base will return a class 
# later we will use this base for creating database models or orm models
Base = declarative_base()


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
