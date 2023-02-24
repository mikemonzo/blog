""" pass """
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, models, database
from ..hashing import Hash

router = APIRouter()

get_db = database.get_db


@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    """ pass """
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(user_id: int, db: Session = Depends(get_db)):
    """ pass """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user
