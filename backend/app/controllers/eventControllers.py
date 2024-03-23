from fastapi import Depends

from models.eventModel import Event
from sqlalchemy.orm import Session

class EventController:
    def getAllEvents(db: Session):
        # return db.query(User).all()
        return "Get All Events"
    
    def getEventDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get Event Detail"