from fastapi import FastAPI
from . import schemas, models
from .database import engin 

app = FastAPI()

models.Base.metadata.create_all(bind=engin)

@app.post('/blog')  
def create(request: schemas.Blog):
    return request
