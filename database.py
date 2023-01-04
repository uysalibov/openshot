from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_model import Users

from typing import Union

engine = create_engine("sqlite:///openshot.db")
Session = sessionmaker(bind=engine)

def sel_userByUsername(username:str):
    """
        Get users filtered by username
    """
    session = Session()
    q = session.query(Users).filter(Users.c.username==username)
    return dict(q[0]) if q.count() > 0 else None
