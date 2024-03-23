from fastapi import Depends

from models.activityModel import Activity
from sqlalchemy.orm import Session

class ActivityController:
    def getAllActivities(db: Session):
        # return db.query(User).all()
        return "Get All Activites"
    
    def getActivityDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get Activity Detail"