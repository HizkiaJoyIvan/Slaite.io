from fastapi import APIRouter, Depends
from controllers.scheduleControllers import ScheduleController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllSchedules():
    return ScheduleController.getAllSchedules()

@router.get("/{id}")
def getScheduleDetail(id):
    return ScheduleController.getScheduleDetail(id)