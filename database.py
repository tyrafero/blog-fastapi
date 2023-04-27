from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




SQL_ALCHEMY_DATABASE_URL= "mysql://admin:admin@localhost:3306/DB?charset=utf8"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

Base= declarative_base()
SessionLocal= sessionmaker(bind=engine,autocommit=False, autoflush=False)