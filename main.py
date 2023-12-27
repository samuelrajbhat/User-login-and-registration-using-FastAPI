from fastapi import FastAPI, Depends, Request, Form
from pydantic import BaseModel
from database import engine, SessionLocal
import models
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# In this we register a user with password and username


app = FastAPI()
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


class UserTable(BaseModel):
    username: str
    password: str
    conform_password: str


# Defining the route to render the form
@app.get("/form_show", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("loginpage.html", {"request": request})


class Login(BaseModel):
    username: str
    password: str


# Defining the route to handle form submission
@app.post("/submit-form")
async def submit_form(username: str = Form(...), password: str = Form(...)):

    return {"Username ": username, "Password ": password}


async def create_item(item: Login):
    obj = UserTable(username=item.username, password=item.password, conform_password=item.password)
    return obj


#

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/signup")
def signupuser(username: UserTable, db: db_dependency):
    if username.password == username.conform_password:
        db_user = models.Todos(username=username.username, password=username.password)
        db.add(db_user)
        db.commit()
        return "User Created successfully"
    else:
        return "Password do not match"
