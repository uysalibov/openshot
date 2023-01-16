from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True)
    username = Column("username", String)
    hashedPass = Column("hashedPass", String)
    
class Projects(Base):
    __tablename__ = "projects"
    
    projectId = Column("projectId", String, primary_key=True)
    ownerId = Column("ownerId", Integer)
    projectName = Column("projectName", String)
    width = Column("width", Integer)
    height = Column("height", Integer)
    fps = Column("fps", Integer)
    sample_rate = Column("sample_rate", Integer)
    channels = Column("channels", Integer)
    channels_layout = Column("channels_layout", Integer)
    
class Files(Base):
    __tablename__ = "files"
    
    Id = Column("Id", Integer, primary_key=True)
    userId = Column("userId", Integer)
    projectId = Column("projectId", String)
    createdAt = Column("createdAt", String)
    type = Column("type", Integer)
