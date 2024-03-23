from fastapi import Depends

from models.scheduleModel import Schedule
from sqlalchemy.orm import Session

class ScheduleController:
    def getAllSchedules(db: Session):
        # return db.query(User).all()
        return "Get All Schedules"
    
    def getScheduleDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get Schedule Detail"