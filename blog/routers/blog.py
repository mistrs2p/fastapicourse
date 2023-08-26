from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('', status_code=status.HTTP_201_CREATED)
# db is session that depends on database
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id of {id} is removed!"}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(request: schemas.Blog, id: int, db: Session = Depends(database.get_db)):
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



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
        # Or
        # respone.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog with the id {id} is not available'}
    return blog

