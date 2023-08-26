from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from .. import models, database, schemas
from ..hashing import Hash


def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Incorrect Password')
    # JWT token
    return user