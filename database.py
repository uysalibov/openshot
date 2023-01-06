from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Union
import uuid

from database_model import Projects, User
from models import Project, User as MUser

engine = create_engine("sqlite:///openshot.db")
Session = sessionmaker(bind=engine)

def sel_userByUsername(username:str):
    """
        Get users filtered by username
    """
    session = Session()
    q = session.query(User).filter(User.username==username)
    return q[0].__dict__ if q.count() > 0 else None

def ins_newProject(request_model: Project, owner: MUser):
    
    session = Session()
    model = request_model.dict()
    name = model.pop("name") # we remove it because our request model and database model have different name
    
    new_project = Projects(
        projectId=str(uuid.uuid4().hex),
        ownerId=owner["id"],
        projectName=name,
        **model
    )
    session.add(new_project)
    session.commit()
    return new_project.projectId
    