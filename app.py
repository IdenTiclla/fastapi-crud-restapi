from typing import Text
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import date, datetime
from uuid import uuid4 as uuid

app = FastAPI()

posts = [
    
]

# Post MOdel

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get('/')
def read_root():
    return {
        "welcome": "welcome to my REST API"
    }

@app.get('/posts')
def get_posts():
    return posts

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    print(post_id)
    
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(status_code=404, detail="Post Not Found.")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)

            return {"message": "Post has been deleted successfully"}

    raise HTTPException(status_code=404, detail="Post Not Found.")


@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]
