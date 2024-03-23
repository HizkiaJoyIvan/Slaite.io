from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from config.database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    detail = Column(String)
    due_time = Column(Time)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    activity = relationship("Relationship", back_populates="activity")
    