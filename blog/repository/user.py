from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..models import User as UserModel
from ..schemas import User as UserSchema
from ..hashing import Hash


def create_user(user: UserSchema, db: Session):
    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_one_user(user_id: int, db: Session):
    user: UserModel = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user
