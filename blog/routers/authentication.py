from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import authentication 

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return authentication.login(request, db)