from fastapi import FastAPI


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
