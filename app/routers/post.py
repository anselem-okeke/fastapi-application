from typing import List, Optional
from sqlalchemy.orm import Session

from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db

import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)
logger = logging.getLogger("uvicorn.error")

@router.get("/", response_model=List[schemas.Post])
def get_post(
        db: Session = Depends(get_db),
        limit:int=10,
        skip:int=0,
        search:Optional[str]="",
        current_user:models.User=Depends(oauth2.get_current_user)
):

    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all() #retrieves all post
    # posts = db.query(models.Post).filter(models.Post.owner_id==current_user.id).all() #retrieves a single post with a specific id
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(
        post: schemas.PostCreate,
        db: Session=Depends(get_db),
        current_user:models.User=Depends(oauth2.get_current_user)):

# def create_posts(
#         post: schemas.PostCreate,
#         db: Session = Depends(get_db),
#         current_user: schemas.TokenData = Depends(oauth2.get_current_user)
# ):
#
#     post_data = post.dict(exclude_unset=True)
#     owner_id = int(current_user.id)

    new_post = models.Post(
        owner_id=current_user.id,
        **post.dict()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.Post)
def get_post(
        id: int,
        db: Session = Depends(get_db),
        current_user:models.User=Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )

    # if post.owner_id != current_user.id:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Not authorized to perform requested action"
    #     ) #retrieves single posts

    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(
        id:int,
        db: Session = Depends(get_db),
        current_user:models.User=Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(
        id: int,
        post:schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    db_post = post_query.first()

    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")

    if db_post.owner_id !=current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    post_query.update(post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()

