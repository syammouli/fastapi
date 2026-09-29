from fastapi import FastAPI
from pydantic import BaseModel
# create a instance of the FastAPI
app = FastAPI()


@app.get("/")
def index():
    return {"data":{"name":"hello world"}}
# above is the path operation function for @app is the instance of FastAPI, and the path operation function is index, which will be called when the client sends a GET request to the root path ("/"). The function returns a JSON response with a key "data" and a nested key "name" with the value "hello world".

@app.get("/hello")
def hellos():
    return {"data":{"name":"about world"}}


@app.get("/show/{id}")
def show(id: int):
    return {"data":{"given_ id":id}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":{"name":"unpublished"}}
# if we are having dynamic render withn same path then we need to put the dynamic path at the end of the path operation function, otherwise it will be considered as a static path and will not work as expected. 
@app.get("/blog/{name}")
def names(name:str):
    return {"data":{"name":name}}

@app.get("/published")
def published(limits: int, published: bool):
    return {"data": {"limits": f"{limits}", "published": f"{published}"}}
# to run this, we need to add in url: http://localhost:8000/published?limits=10&published=true
# we can also define the query parameters with default values, which will be used if the client does not provide a value for that parameter. For example: like using optional parameters with default values, we can define a query parameter with a default value like this:


# handle default path parameters with default values 
# def published(limits: int = 10, published: bool = True):

@app.get("/items/{item_id}")
def read_items(item_id: int, limits: int):
    return {"data": {"item_id": item_id, "limits": f"{limits}"}}

# Here the query parameter is "limits"  and item_id is a path parameter, and both are required parameters. If the client does not provide a value for "limits", it will return an error. We can also make "limits" an optional parameter by providing a default value like this:
class Blog(BaseModel):
    name:str
    age:int
@app.post("/postCheck")
def post_check(blog:Blog):
    return { "data" :{"name": f"{blog.name}", "age": f"{blog.age}"}}

