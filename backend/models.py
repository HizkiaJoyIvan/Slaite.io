from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    schedules = relationship("Schedule", back_populates="user", uselist=False)

class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="schedule")
    activities = relationship("Activity", back_populates="schedule")

class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    schedule = relationship("Schedule", back_populates="activity")
    schedule = relationship("Schedule", back_populates="activity", uselist=False)
    schedule = relationship("Schedule", back_populates="activity", uselist=False)

class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    status = Column(String)
    time = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    activity_id = Column(Integer, ForeignKey('activity.id'))

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    detail = Column(String)
    due_time = Column(Time)
    repeat_interval = Column(Enum("Daily", "Weekly", "Monthly"))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    repeat_interval = Column(Enum("Daily", "Weekly", "Monthly"))
    schedule_id = Column(Integer, ForeignKey('schedule.id'))



