from sqlalchemy import Enum, Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.database import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    repeat_interval = Column(Enum("Daily", "Weekly", "Monthly", name="repeat_interval_enum"))
    schedule_id = Column(Integer, ForeignKey('schedules.id'))
    notification = relationship("Notification", back_populates="activity", passive_deletes=True)
    schedule = relationship("Schedule", back_populates="activities")
    event  = relationship("Event", back_populates="activity", uselist=False, passive_deletes=True)
    task = relationship("Task", back_populates="activity", uselist=False, passive_deletes=True)
