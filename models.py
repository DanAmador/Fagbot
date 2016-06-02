from sqlalchemy import Column, ForeignKey, String, Integer,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(String(4096), nullable=False)
    sender = Column(Integer, ForeignKey('sender.id'))
    chat = Column(Integer, ForeignKey('chat.id'))
    date = Column(Date)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=True)
    date = Column(Date)

class Chats(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    userIds = relationship(Users)
    type = Column(String(40), nullable=True)
    title = Column(String(40), nullable=False)
    date = Column(Date)
