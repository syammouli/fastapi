from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schema,database
from sqlalchemy.orm import Session
from ..database import get_db
from blog.oauth2 import get_current_user
router = APIRouter(
    prefix="/blog",
    tags=["this below get api is getting imported from blog.routes.blog using router"]
)

@router.get("/getdatas",status_code=status.HTTP_202_ACCEPTED)
def get_data(db: Session = Depends(database.get_db), current_user: schema.TokenData = Depends(get_current_user)):
    posts = db.query(models.Post).all()
    return posts

