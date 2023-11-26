from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql


db_uri = 'mysql+pymysql://root:@localhost/burnout_db'
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
