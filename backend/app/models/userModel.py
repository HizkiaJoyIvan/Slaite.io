from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from config.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    schedules = relationship("Schedule", back_populates="user", uselist=True, passive_deletes=True)
    notifications = relationship("Notification", back_populates="user", uselist=True, passive_deletes=True)