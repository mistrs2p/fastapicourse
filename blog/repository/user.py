from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from .. import models, database, schemas
from ..hashing import Hash


def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id of {id} not found")
    return user