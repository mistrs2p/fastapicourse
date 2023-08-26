from fastapi import APIRouter, Depends
from .. import schemas, database, oauth2
# from typing import List
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(prefix='/user', tags=['Users'])


@router.post('')
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id, db)
