from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog.JWTtoken import verify_token

# This is saying where you want to access the toke, that is called the url
# we are going to take the token from login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # this is going to decode the toke, or verify the token
    ''' This is going to decoding the tokens we are having '''
    
    return verify_token(token,credentials_exception)
