from fastapi import FastAPI
from . import models
from .database import engin
from .routers import blog, user, authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engin)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
