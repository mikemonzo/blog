""" pass """
from typing import List

from blog import schemas, database, oauth2
from blog.repository import blog
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

get_db = database.get_db
get_current_user = oauth2.get_current_user


# CREAT
@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowBlog
)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    """ pass """
    return blog.create_blog(request, db)


# READ
@router.get(
    '/',
    response_model=List[schemas.ShowBlog]
)
def get_all_blog(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    """ pass """
    return blog.get_all_blogs(db)


@router.get(
    '/{blog_id}',
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog
)
def get_one_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    """ pass """
    blog_query = blog.get_one_blog(blog_id, db)
    return blog_query


# UPDATED
@router.put(
    '/{blog_id}',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.ShowBlog
)
def update_one_blog(
        blog_id: int,
        request: schemas.Blog,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user)
):
    """ pass """
    return blog.update_blog(blog_id, request, db)


# DELETE
@router.delete(
    '/{blog_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_one_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    """ pass """
    return blog.delete_blog(blog_id, db)



