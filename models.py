from pydantic import BaseModel
from typing import Union

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    id: int
    username: str
    
class Project(BaseModel):
    name: str
    width: int
    height: int
    fps: int = 30
    sample_rate: int = 44100
    channels: int = 2 # Audio channels (2 = stereo)
    channels_layout: int = 3  # Channel layout type (3=stereo, 4=mono, 7=Surround)

class UserInDB(User):
    hashed_password: str
    
class ProjectId(BaseModel):
    project_id: str