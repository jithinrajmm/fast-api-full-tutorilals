from fastapi import APIRouter,status,Response,Depends,HTTPException,Path
from sqlalchemy.orm import Session
from blog import models
from blog import database
from blog import schemas
from typing import List
from blog.repositories import blog_repository

# this is for the getting the current user token
from blog.oauth2 import get_current_user

# api router operations
routers = APIRouter(
prefix='/blog',
  tags=['BLOGS']  
)

# ###########################################################################################################  
# this is for getting all the blogs to the databasex

@routers.get('/all_blogs',response_model=List[schemas.BlogsAllList],status_code=status.HTTP_200_OK)
def get_all_blogs(response:Response,db: Session = Depends(database.get_db),current_user: schemas.UserSchema = Depends(get_current_user)):
    
    return blog_repository.get_all_blogs(response,db)

# ###########################################################################################################  
# this is for creating the blog

@routers.post('/create_blog',status_code=status.HTTP_201_CREATED)
def create_blog(blogs: schemas.Blogs,db: Session = Depends(database.get_db),current_user: schemas.UserSchema = Depends(get_current_user)):
    ''' used to store the blog to the data base '''
    # please check the repositories folder for showing the below fuction
    return blog_repository.create_blog(blogs,db)
    
############################################################################################################ 
#This is used to show the single blogs

@routers.get('/{id}',status_code=status.HTTP_302_FOUND,response_model=schemas.ShowBlogs)
def get_single_blog(response: Response,id:int = Path(description='Expecting a Int id value'),
                        db:Session = Depends(database.get_db),
                        current_user: schemas.UserSchema = Depends(get_current_user)):
    blog = db.query(models.Blogs).filter(models.Blogs.id==id).first()
    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {'Detail': 'Blog with this id is not existing'}
    
    # instead of the abobe method we can also use the HTTPException method   
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found , Please check the id')
    return blog
    
############################################################################################################ 

# This is for the deleting the post
@routers.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int =Path(description='Expecting a integer value'),db:Session = Depends(database.get_db),current_user: schemas.UserSchema = Depends(get_current_user)):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    
    if  not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{ id } is not present in the storage')
    else:
        blog.delete(synchronize_session=False)
            
        db.commit()
        return {'Detail': "deleted success fully"}

####################################################################################################################
# Update the single blog
@routers.put('/update/{blog_id}')
def update_blog(blog_id:int,request_body: schemas.BlogsUpdate,db:Session = Depends(database.get_db),current_user: schemas.UserSchema = Depends(get_current_user)):
    # blog = db.query(models.Blogs).filter(models.Blogs.id == blog_id).update(request_body.dict())
    blog = db.query(models.Blogs).filter(models.Blogs.id == blog_id).first()
    
    if blog:
        for key, value in request_body.dict().items():
            if value is not None:
                setattr(blog,key,value)
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Sorry,The id {blog_id} is not found')
#####################################################################################################################