from fastapi import APIRouter, Depends
from controllers.notificationControllers import NotificationController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllNotification():
    return NotificationController.getAllNotification()

@router.get("/{id}")
def getNotificationDetail(id):
    return NotificationController.getNotificationDetail(id)