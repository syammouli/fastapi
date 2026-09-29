from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import database, schema,models
# from blog.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import Hash
from ..repository.user import destroy
from ..token import create_access_token
router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)
@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email")

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    # return {"message": "Login successful", "user": user.name, "email": user.email}

    access_token= create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}