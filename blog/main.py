# from asyncio.base_subprocess import ReadSubprocessPipeProto
# from fastapi import FastAPI
# from blog import schemas
# from blog import models
# from fastapi import Path
# # this for the status code in fast api
# from fastapi import status

# # This is for the custom response creation
# from fastapi import Response

# from blog.database import Base, SessionLocal
# from blog.database import engine
# # from blog.models import Blogsss



# # this is for the password hashing purpose
# from passlib.context import CryptContext
# # for creating an element to the database , or row to the database with value we need the session from the 
# # sqlalchemy.orm import Session
# from sqlalchemy.orm import Session
# from fastapi import Depends
# from blog.database import SessionLocal

''' ALL THE ABOVE DEPENDECIES FOR THE CODE WHICH COMMENTED BELOW 😀😀😀😀😀😀😀😀'''

#=================================================================================================================
from fastapi import FastAPI
from blog import models
from blog.database import engine
# this is for the routing 
from blog.routers import blogs

# this is for the user routing
from blog.routers import user

# this is for the Authentication
from blog.routers import authentication

app = FastAPI()

# integrating all other parts from here 
# This code is going to create tabel in the data base 
# remember the things , this code is executing an creating the table in the models
models.Base.metadata.create_all(bind=engine)

''' this is the routing for the Authentication'''
app.include_router(authentication.routers)

''' this is routing the app to the router '''
app.include_router(blogs.routers)

''' this is routing for the user '''
app.include_router(user.routers)



#=================================================================================================================






''' all the below code is my practiced code you can check the neet code in blog/routers
int this folder containing some files , schemas, database, models is important'''

# def get_db():
#     '''This is used to connect with the database and making the session as the pydantic thing'''
#     db = SessionLocal()
#     # The session local is from the database.py
#     try:
#         yield db
#     finally:
#         db.close()



# Depends(get_db) this is going to convert the session into pydantic things
# get_db is the function connection
# actually the depends is the dependency of the session, 
# we need independent database conncetion or session per each reqeust, use the session for all the same request
# when one reqeust is closed that session also destroyed , 
# for the new requests it creating another one 

##############################################################################################################

# @app.post('/create_blog',status_code=status.HTTP_201_CREATED,tags=['BLOGS'])
# def create_blog(blogs: schemas.Blogs,db: Session = Depends(get_db)):
#     ''' used to store the blog to the data base '''
#     new_blog = models.Blogs(title=blogs.title,body=blogs.body,published=blogs.published,user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

##############################################################################################################
    
''' for handling the errors we have the another option is callde HTTPException '''
from fastapi import HTTPException

# This is moved to the routers => blogs.py 
# @app.get('/all_blogs',status_code=status.HTTP_200_OK,tags=['BLOGS'])
# def get_all_blogs(response:Response,db: Session = Depends(get_db)):
    
#     blogs = db.query(models.Blogs).all()
#     if not blogs:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'Detail': "not data avalilable "}
#     return blogs
    
########################################################################################################################  
# This is used to get the single blog

# from blog.schemas import ShowBlogs  
# @app.get('/blog/{id}',status_code=status.HTTP_302_FOUND,tags=['BLOGS'],response_model=ShowBlogs)
# def get_single_blog(response: Response,id:int = Path(description='Expecting a Int id value'),db:Session = Depends(get_db)):
#     blog = db.query(models.Blogs).filter(models.Blogs.id==id).first()
#     # if not blog:
#     #     response.status_code = status.HTTP_404_NOT_FOUND
#     #     return {'Detail': 'Blog with this id is not existing'}
    
#     # instead of the abobe method we can also use the HTTPException method   
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found , Please check the id')
#     return blog
     
######################################################################################################################## 
    
# STATUS CODE HANDLING
# THERE ARE TWO WAYS TO HANDEL THE RESPONSE
# ONE IS IMPORT THE Reqeust from the fastapi
# second one is import the HTTPException

######################################################################################################################## 
# # This is for the deleting the post
# @app.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['BLOGS'])
# def delete_post(id: int =Path(description='Expecting a integer value'),db:Session = Depends(get_db)):
#     blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    
#     if  not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{ id } is not present in the storage')
#     else:
#         blog.delete(synchronize_session=False)
            
#         db.commit()
#         return {'Detail': "deleted success fully"}
######################################################################################################################## 

# from blog.schemas import BlogsUpdate

# update the single blog 
# @app.put('/update/{blog_id}',tags=['BLOGS'])
# def update_blog(blog_id:int,request_body: BlogsUpdate,db:Session = Depends(get_db)):
#     # blog = db.query(models.Blogs).filter(models.Blogs.id == blog_id).update(request_body.dict())
#     blog = db.query(models.Blogs).filter(models.Blogs.id == blog_id).first()
    
#     if blog:
#         for key, value in request_body.dict().items():
#             if value is not None:
#                 setattr(blog,key,value)
#         db.add(blog)
#         db.commit()
#         db.refresh(blog)
#         return blog
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Sorry,The id {blog_id} is not found')
        
# Response models
# the response models is a model or schema is used to disply the essential information to the user
# suppose we dont want to display the id of the blog we can hide from this response_model = pydantic schema
# for that we need to define the pydantic schema 
# just inheriting the pydantic schema of the reqeust body, just look at the file schemas.py

# from blog.schemas import BlogsResponseSchema

# if we are using the response_model as a schema we need to tell the query config inside of the schemas.py 
#  here BlogsResponseSchema

# @app.get('/response_model_blog/{id}',response_model=BlogsResponseSchema,tags=['BLOGS'])
# def response_model_blog(id: int,db: Session = Depends(get_db)):
#     blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
#     return blog
    
# from typing import List
# from blog.schemas import BlogsAllList

# we are just going to show only the title ,body, published in teh item from the list of items
# for that we need to use the List from the fastapi    
# @app.get('/get_all',response_model=List[BlogsAllList],tags=['BLOGS'])
# def get_all(db:Session= Depends(get_db)):
#     ''' we cant use the response_model = schema name directly
#     its because of the blogs (below) contains a list of values ,
#     for the we have used the List type from the typing in path 
#     operation decorator. after the List is we defined the schema or responseModel name
#     within squere [] braces , please care about that '''
#     blogs = db.query(models.Blogs).all()
#     return blogs
    
    


# user creation and management next topic

# this is for the passwoed hashing for that we have used passlib library
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# please notice the imports 
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# This is for the reqeust body in path operation function parameter
# from blog.schemas import UserSchema

# this is for the response_model in path operation query parameter
# from blog.schemas import UserViewSchema

####################################################################################################################
# For the user creations 
# @app.post('/user_create',response_model=UserViewSchema,tags=['USERS'])
# def user_create(request_user:UserSchema,db:Session = Depends(get_db)):
    
#     ''' This method is going to create user , its is post method, in the path operation function we need to tell the 
#     schema , Its from the Schema files '''
     
#     hashed_password = pwd_context.hash(request_user.password)
#     user = models.User(name=request_user.name,email = request_user.email, password = hashed_password)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
    
 ####################################################################################################################   


####################################################################################################################   
# get all users
# @app.get('/users',response_model=List[schemas.UserViewSchema],tags=['USERS'])
# def all_users(db:Session=Depends(get_db)):
    
#     users = db.query(models.User).all()
#     if users:
#         return users
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No users is available')
####################################################################################################################       



#################################################################################################################### 
# Get single user  
# @app.get('/user/{user_id}',response_model=UserViewSchema,tags=['USERS'])
# def get_user(user_id:int,db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user:
#         return user
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {user_id} is not exists')
####################################################################################################################   