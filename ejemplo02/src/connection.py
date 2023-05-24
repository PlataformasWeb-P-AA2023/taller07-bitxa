from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///taller07.db')

def get_engine():
    return engine

def create_session():
    return sessionmaker(bind=engine)()

def get_session():
    return create_session()

