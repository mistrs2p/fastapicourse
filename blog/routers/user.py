from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
# from typing import List
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/user', tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        name= request.name,
        email= request.email,
        password= Hash.bcrypt(request.password)
    )
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def show_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id of {id} not found")
    return user