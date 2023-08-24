from fastapi import Depends, FastAPI, HTTPException, status, Response
from . import schemas, models
from .database import SessionLocal, engin 
from sqlalchemy.orm import Session
app = FastAPI()

# Create database or add col to the database
models.Base.metadata.create_all(bind=engin)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=status.HTTP_201_CREATED)  
# db is session that depends on database
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', status_code=status.HTTP_200_OK)  
def all(db: Session = Depends(get_db)):
    # quereing on model
    blogs = db.query(models.Blog).all()
    return blogs
   
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)  
def show(id: int, respone: Response,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with the id {id} is not available')
        # Or
        # respone.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog with the id {id} is not available'}
    return blog
   
