from datetime import datetime, timedelta
from typing import Union
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm

from models import Token, User, Project, ProjectId
from auth import (
    authenticate_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user,
    check_project_id
)
from database import ins_newProject

app = FastAPI()

@app.post("/token", response_model=Token, tags=["Authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"Authorization": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User, tags=["Authentication"])
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/projects/new", tags=["projects"])
async def new_project(current_user: User = Depends(get_current_user), project_details: Project = Depends()):
    r = ins_newProject(project_details, current_user)
    return {"projectId": f"{r}"}

@app.post("/files/new", tags=["files"])
async def new_file(current_user: User = Depends(get_current_user), file: UploadFile = File(...), project_id: Project = Depends(check_project_id)):
    filecontent = await file.read()
    
    return {"a": file.filename, "b": file.content_type, "c": filecontent}
    
    

        
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)