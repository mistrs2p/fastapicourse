from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI as imported above
# uvicorn main:app 'main as the filename and app as the FastAPI instance'
app = FastAPI()

# operation on the path like Get and the route
# the function is path operation function


@app.get('/')
def index():
    return {
        "data": {
            "name": 'mahdi'
        }
    }

# set query params like /blog?limit=53


@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:

        return {
            "data": f"blogs: {limit} and published: {published}"
        }
    else:
        return {
            "data": f"blogs: {limit}"
        }


@app.get('/blog/unpublished')
def unpublished():
    return {
        "data": "unpublished"
    }


@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": {
            "name": 'Blog id is ' + f'{id}',
            id: id
        }
    }


@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": {
            "name": 'Blog id is ' + f'{id}',
            id: id
        }
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(requset: Blog):
    return {'data': 'blog is created'}
