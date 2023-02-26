from blog.models import Blog as BlogModel
from blog.schemas import Blog as BlogSchema
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def get_all_blogs(db: Session):
    blogs = db.query(BlogModel).all()
    return blogs


def create_blog(request: BlogSchema, db: Session):
    new_blog = BlogModel(
        title=request.title,
        body=request.body,
        user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_one_blog(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {blog_id} is not available'
        )
    return blog


def delete_blog(blog_id, db):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_blog(blog_id, request, db):
    blog: BlogModel = db.query(BlogModel).filter(BlogModel.id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {blog_id} not found"
        )
    blog.update(request.dict())
    db.commit()
    return None
