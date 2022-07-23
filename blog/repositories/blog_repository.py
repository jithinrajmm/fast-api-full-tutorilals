from sqlalchemy.orm import Session
from blog import models,schemas
from fastapi import Response,status

# getting the all blogs


def get_all_blogs(response:Response,db:Session):
    blogs = db.query(models.Blogs).all()
    print(blogs)
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Detail': "not data avalilable "}
    return blogs
    
def create_blog(blogs:schemas.Blogs,db:Session,):
    new_blog = models.Blogs(title=blogs.title,body=blogs.body,published=blogs.published,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog