from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base  # importing Base before models not after...create_all only creates tables for models that exists at the time it is called 
from models.library import Library
from models.owner import LibraryOwner
from models.member import Member
from models.book import Book


DATABASE_URL = "sqlite:///library.db"

# Setting up SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, echo=False)#engine is the connection b2n python and the database 
Session = sessionmaker(bind=engine)

# creates the tables after models are imported 
Base.metadata.create_all(engine)  #if you call Base.metadata.create_all(engine) before importing models, Base.metadata doesn’t know about them yet.


#models/ folder must have an __init__.py file, even if it’s empty.
#This tells Python to treat models/ as a package so main.py can import models.