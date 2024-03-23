from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from config.database import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String)
    status = Column(String)
    time = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))
    user = relationship("User", back_populates="notifications")
    activity = relationship("Activity", back_populates="notification")
