from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, Request
from .. import models, database, schemas, token
from ..hashing import Hash
from datetime import timedelta

# def login(request: schemas.Login, db: Session = Depends(database.get_db)):


def login(request: Request, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Incorrect Password')
    # JWT token
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
