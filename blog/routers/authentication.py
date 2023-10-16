from fastapi import APIRouter, Depends, HTTPException, status
# from typing import Annotated
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import authentication
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])


@router.post('/login')
# def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return authentication.login(request, db)
