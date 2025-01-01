# User model definition
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    creativity = Column(Float, default=0.0)
    inspiration = Column(Float, default=0.0)
    diligence = Column(Float, default=0.0)
    fame = Column(Float, default=0.0)
    tokens = Column(Float, default=0.0)
