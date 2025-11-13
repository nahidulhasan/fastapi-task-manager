from fastapi import FastAPI
from .database import engine
from . import models
from .routers import auth, tasks

# create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Task Manager")

app.include_router(auth.router)
app.include_router(tasks.router)
