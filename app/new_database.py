# import time
# from random import randint
# from typing import Optional
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
#
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# # from fastapi.params import Body
# from pydantic import BaseModel
# from sqlalchemy.testing.plugin.plugin_base import logging
#
# from . import models
# from .database import engine, get_db
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='12345', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull...")
#         break
#     except Exception as error:
#         print("Connection to the database failed")
#         print("Error: ", error)
#         time.sleep(2)

# @app.get("/sqlalchemy")
# def get_posts(db: Session = Depends(get_db)):
#     print("GET /lal endpoint was called")
#     posts = db.query(models.Post).all()
#     print(f"GET /lal called, returning {posts}")
#     return {"Data":posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post:Post, db: Session = Depends(get_db)):
#
#     new_post = models.Post(
#         title=post.title, content=post.content, published= post.published)
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#
#     return {"data": new_post}
#
# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
#     post = cursor.fetchone()
#
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message":f"post with id: {id} was not found for not all "}
#     return {"post_detail": post}
#
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_posts(id:int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#
#     if deleted_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id:{id} was not found")
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
#
#
# @app.put("/posts/{id}")
# def update_post(id:int, post:Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#                    (post.title, post.content, post.published, (str(id),)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#
#     if updated_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id:{id} was not found")
#
#     return {"Data": updated_post}
#
#
#
#
#
