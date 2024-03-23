from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from config.database import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    activity = relationship("Relationship", back_populates="activity")
