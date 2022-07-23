from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from blog import schemas,database,models

# This is for the hashing password
from blog.hashing import Hashing



# APIRouter operation , first is tag
routers = APIRouter(
  tags=['USERS']  
)


################################################################################################################
@routers.post('/user_create',response_model=schemas.UserViewSchema)
def user_create(request_user:schemas.UserSchema,db:Session = Depends(database.get_db)):
    
    ''' This method is going to create user , its is post method, in the path operation function we need to tell the 
    schema , Its from the Schema files '''
     
    hashed_password = Hashing.hashing(request_user.password)
    user = models.User(name=request_user.name,email = request_user.email, password = hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
    
################################################################################################################

################################################################################################################
# Get single user  
@routers.get('/user/{user_id}',response_model=schemas.UserViewSchema)
def get_user(user_id:int,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {user_id} is not exists')
################################################################################################################


################################################################################################################   
# get all users
@routers.get('/users',response_model=List[schemas.UserViewSchema])
def all_users(db:Session=Depends(database.get_db)):
    
    users = db.query(models.User).all()
    if users:
        return users
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No users is available')
################################################################################################################  