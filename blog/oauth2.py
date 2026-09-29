
from fastapi.params import Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
from . import token as token_service

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,       
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token_service.verify_token(token, credentials_exception)

# the above code is used to get the current user from the token. We are using the OAuth2PasswordBearer class from the fastapi.security module to create a dependency that will extract the token from the request and pass it to the get_current_user function.
#  The get_current_user function will then verify the token and return the user information if the token is valid.
#  If the token is invalid, it will raise an HTTPException with a 401 status code.