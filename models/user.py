from sqlalchemy import String, Integer, Column
from core.database import Base

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)