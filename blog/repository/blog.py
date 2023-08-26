from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from .. import  models, database
def get_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs