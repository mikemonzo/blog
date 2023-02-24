""" pass """
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, models, database

router = APIRouter()

get_db = database.get_db


@router.post(
    '/blog',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowBlog,
    tags=['blogs']
)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    """ pass """
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get(
    '/blog',
    response_model=List[schemas.ShowBlog],
    tags=['blogs']
)
def get_all_blog(db: Session = Depends(get_db)):
    """ pass """
    blogs = db.query(models.Blog).all()
    return blogs


@router.get(
    '/blog/{blog_id}',
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
    tags=['blogs']
)
def get_one_blog(blog_id: int, db: Session = Depends(get_db)):
    """ pass """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {blog_id} is not available'
        )
    return blog


@router.delete(
    '/blog/{blog_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    tags=['blogs']
)
def delete_one_blog(blog_id: int, db: Session = Depends(get_db)):
    """ pass """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put(
    '/blog/{blog_id}',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.ShowBlog,
    tags=['blogs']
)
def update_one_blog(blog_id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    """ pass """
    blog_query = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    blog_query.update(blog.dict())
    db.commit()
    return blog
