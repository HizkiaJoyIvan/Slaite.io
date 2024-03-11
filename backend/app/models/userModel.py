from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from config.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    schedules = relationship("Schedule", back_populates="user", uselist=False)