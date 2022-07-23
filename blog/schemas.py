from pydantic import BaseModel
from typing import Optional,List


class Blogs(BaseModel):
    ''' This is used to post the blog,
    Also we need to inherit this class for showing the all  blogs which related to the user
     '''
    title : str
    body : str

    published : Optional[bool] = False
    

#########################################################################################   

class UserBlogs(Blogs):
    ''' This class is used to show the all blogs of a purtilcular user when we fetching
    a user with id, for that we need to add the config file also ,
    this class is writed for setting the feild of the below class, the feild is blogs'''
    
    class Config:
        orm_mode = True
        
class UserViewSchema(BaseModel):
    ''' this class is used to show the user detail while fetching with id of the user, we need
    to show the all blogs which related to the selected user '''
    name : str
    email: str
    blogs: List[UserBlogs] = []
    class Config:
        orm_mode = True
        
class UserView(BaseModel):
    ''' This Class  used to show the user details , this class is using below ShowBlogs class , 
    for the feild of the creator 
     '''
    name: str
    email: str
    class Config:
        orm_mode = True
# This Schema is used to show the creator details and blogs 
# Remeber only for viewing 
# class Blogs(BaseModel):
    # title : str
    # body : str
    # published : Optional[bool] = False
# The showBlogs schema is iherited from the Blogs schema
class ShowBlogs(Blogs):
    creator : UserView
    class Config:
        orm_mode = True
    
    
########################################################################################
    
    
class BlogsUpdate(BaseModel):
    
    ''' This is for the updating of a single blog docs'''
    
    title : Optional[str]=None
    body : Optional[str]=None
    published : Optional[bool] = False
    
    
class BlogsResponseSchema(BaseModel):
    
    ''' this schema is used to the response_model
    Here i am going to hide the Published status, and id of the blog from view
    ,Notice that the configuration thats setted inside of this class,
    used to hiding some of the feild from the blogs means published = Fasle is hiding'''
    
    title: str
    body: str
    class Config:
        orm_mode = True
        
        
class BlogsAllList(BaseModel):
    title: str
    body: str
    published: bool
    
    creator: UserView
    
    class Config:
        orm_mode = True
        
#This is for the user creation schema 
class UserSchema(BaseModel):
    name : str
    email : str
    password: str
    
# This is for the user authentication schema
class UserAuth(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True
    

# this is for the jwt token

class Token(BaseModel):
    access_token :str
    token_type : str
    
class TokenData(BaseModel):
    email: Optional[str] = None
        
     