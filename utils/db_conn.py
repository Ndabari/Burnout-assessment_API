from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_uri = 'postgresql://okoyo:password@192.168.184.131/burnout-db'
engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

