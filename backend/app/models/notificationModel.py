from sqlalchemy import Boolean, Enum, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    status = Column(String)
    time = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    activity_id = Column(Integer, ForeignKey('activity.id'))