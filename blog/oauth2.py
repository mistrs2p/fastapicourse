from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from .token import verify_token
import token
# tokenUrl set route, where i want to fetch token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(current_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(current_token, credentials_exception)
    # return user
