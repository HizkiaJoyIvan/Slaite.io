from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    repeat_interval = Column(Enum("Daily", "Weekly", "Monthly"))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))