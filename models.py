from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Blog(Base):
    __tablename__ = 'Blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16), index=True)
    user_id = Column(Integer, ForeignKey('User.id'))

    author = relationship('User', back_populates='blogs')
    # body= Column(String(50), index=True, nullable= True)

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    
    blogs = relationship('Blog', back_populates='author')