from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    user_id: int

    class Config:
        orm_mode = True

class Blog(BlogCreate):
    id: int
    


class UserCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class User(UserCreate):
    id: int
    

