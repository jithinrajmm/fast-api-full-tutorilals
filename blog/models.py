from blog.database import Base
from sqlalchemy import Column,String,Integer,Float,Boolean,ForeignKey

# THIS IS USED TO CREATING THE DATABASE RELATIONSHIP BETWEEN TWO TABLES
# LIKE FOREIGN KEY REALTIONS ----> 😁😁😁😁😁😁
from sqlalchemy.orm import relationship


class Blogs(Base):
    # table name is the name of the table which used in the database
    # mainly its using in the relationship
    __tablename__ = 'blogs'
    
    # feilds in the database
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    
    user_id = Column(Integer,ForeignKey('users.id'))
    
    creator = relationship('User',back_populates='blogs')
    
    
    
# This is the models for the user

class User(Base):
    
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key = True, index= True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship('Blogs',back_populates = 'creator')
    