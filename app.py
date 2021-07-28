from typing import Text
from fastapi import FastAPI
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

@app.post('/posts')
def save_post(post: Post):
    print(type(uuid()))
    post.id = str(uuid())
    print(post.dict())
    return posts.append(post.dict())