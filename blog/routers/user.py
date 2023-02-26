""" pass """
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    """ pass """
    return user.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """ pass """
    return user.get_one_user(user_id, db)
