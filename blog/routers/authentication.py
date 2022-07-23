from fastapi import APIRouter,Depends,HTTPException,status
from blog import schemas,database,models
from sqlalchemy.orm import Session
from blog.hashing import Hashing
from datetime import timedelta,datetime
from blog.JWTtoken import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordRequestForm 



routers = APIRouter(
    tags=['AUTHENTICATION']
)

''' just changed the line 
def authentication(request:schemas.UserAuth,db:Session = Depends(database.get_db)):
    '''
@routers.post('/login')
def authentication(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    print(request)
    
    user = db.query(models.User).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user {request.email} not registered')
        
    if not Hashing.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,detail='Incorrect password')
    
    # Generate jwt token and return it 
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # access_token = create_access_token(
        # data={"sub": user.email}, expires_delta=access_token_expires
        # )
    access_token = create_access_token(
        data={"sub": user.email}
        )
    
    return {"access_token": access_token, "token_type": "bearer"}