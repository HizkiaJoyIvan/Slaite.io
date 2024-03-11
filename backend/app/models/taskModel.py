from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    detail = Column(String)
    due_time = Column(Time)
    repeat_interval = Column(Enum("Daily", "Weekly", "Monthly"))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))