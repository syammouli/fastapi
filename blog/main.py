from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from blog.routes import authentication
from . import models, schema
from .database import engine, sessionLocal, get_db
from .hashing import Hash
from .repository import user as userFromRepo

models.Base.metadata.create_all(bind=engine)
from .routes import blog, user
app = FastAPI()


# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


app.include_router(authentication.router)
app.include_router(blog.router)



@app.post("/createdata", tags=["user"])
def create_data(request: schema.Post, db: Session = Depends(get_db)):
    new_post = models.Post(
        title=request.title,
        content=request.content,
        user_id=1
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# @app.get("/getdata",status_code=status.HTTP_202_ACCEPTED, tags=["blog post"])
# def get_data(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts



@app.get("/gettitledata",status_code=status.HTTP_202_ACCEPTED,response_model=List[schema.showonlytittle], tags=["blog post"])
def get_title_data(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all() 
    return posts



@app.get("/getdata/{id}", tags=["blog post"],response_model=schema.Post)
def get_data_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
        # return {"error": status.HTTP_404_NOT_FOUND, "message": f"Post with id {id} not found"}

    return post


@app.delete("/delete/{id}", tags=["user"])
def delete_data(id: int, db: Session = Depends(get_db)):
    return userFromRepo.destroy(id, db)

    # post = db.query(models.Post).filter(models.Post.id == id).first()
    # if not post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    # db.delete(post)
    # db.commit()
    # return {"message": f"Post with id {id} has been deleted"}


@app.put("/update/{id}", tags=["user"])
def update_data(id: int, request: schema.Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.title = request.title
    post.content = request.content
    db.commit()
    db.refresh(post)
    return post


@app.post("/createUser", response_model=schema.user, tags=["user"])
def createUser(request: schema.user, db: Session = Depends(get_db)):

    password_hash =Hash.bcrypt(request.password)
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=password_hash
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/getUser", response_model=List[schema.user], tags=["user"])
def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
# in above line, we are creating the tables in the database using the models defined in the models.py file. The create_all() method will create all the tables defined in the models.py file if they do not exist already. The bind=engine argument is used to specify the database engine to use for creating the tables. In this case, we are using the engine defined in the database.py file, which is connected to a PostgreSQL database.
@app.post("/posting/{pid}", tags=["example"])
def posting(pid:int,name:str):
    return {"data":{"pid":f"{pid}","name":f"{name}"}}

@app.post("/schemaimport", tags=["example"])
def schema_import(request:schema.Blot):
    return {"name in schema is ": f"{request.name}"}