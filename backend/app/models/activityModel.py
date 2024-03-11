from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    schedule = relationship("Schedule", back_populates="activity")