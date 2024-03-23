from fastapi import Depends

from models.notificationModel import Notification
from sqlalchemy.orm import Session

class NotificationController:
    def getAllNotification(db: Session):
        # return db.query(User).all()
        return "Get All Notification"
    
    def getNotificationDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get Notification Detail"