from fastapi import Depends, FastAPI, HTTPException, status, Response
from . import schemas, models
from .database import SessionLocal, engin
from sqlalchemy.orm import Session
from typing import List
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


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id of {id} is removed!"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(request: schemas.Blog, id: int, db: Session = Depends(get_db)):
    # db.query(models.Blog).filter(models.Blog.id == id).update({
    #     models.Blog.title: request.title,
    #     models.Blog.body: request.body
    # }, synchronize_session=False)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.update(request)
    db.commit()
    return {"detail": f"Blog with id of {id} is updated!"}


@app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    # quereing on model
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
        # Or
        # respone.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog with the id {id} is not available'}
    return blog
