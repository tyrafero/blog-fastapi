from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
from models import Blog, User
from fastapi import HTTPException
import schemas,models

app = FastAPI()

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

models.Base.metadata.create_all(engine) #migrating

@app.post('/blog', response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(getdb)):
    print("blog create called")
    db_blog = Blog(title=blog.title, user_id = blog.user_id)
    db.add(db_blog)
    db.commit()
    print("blog committed")
    db.refresh(db_blog)
    return db_blog


@app.post('/user', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(getdb)):
    db_user = User(name = user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# @app.get('/blog/{blog_id}', response_model=schemas.Blog)
# def show_blog(blog_id: int, db: Session = Depends(getdb)):
#     db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
#     if not db_blog:
#         raise HTTPException(status_code=404, detail='Blog not found')
#     return db_blog.__dict__

# @app.get('/blog/list', response_model=List[schemas.Blog])
# def list_blogs(db: Session = Depends(getdb)):
#     blogs = db.query(Blog).all()
#     return blogs.__dict__
