from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="posts")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    posts = relationship(
        "Post",
        back_populates="creator",
        cascade="all, delete"
    )
# here we have defined two models, Post and User, which will be used to create the tables in the database. The Post model has three columns: id, title, and content. The User model has four columns: id, name, email, and password. We have also defined a relationship between the two models using the relationship function from SQLAlchemy. This will allow us to easily access the posts created by a user and the creator of a post.   