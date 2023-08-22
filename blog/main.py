from fastapi import Depends, FastAPI
from . import schemas, models
from .database import SessionLocal, engin 
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind=engin)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')  
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')  
def all(db: Session = Depends(get_db)):
    # quereing on model
    blogs = db.query(models.Blog).all()
    return blogs
   
@app.get('/blog/{id}')  
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
   
