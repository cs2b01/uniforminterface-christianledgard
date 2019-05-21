from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class UsersDB(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('id'), primary_key=True)
    nombre = Column(String(20))
    apellido = Column(String(20))
    password = Column(String(30))
