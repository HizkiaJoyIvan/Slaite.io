from fastapi import APIRouter, Depends
from controllers.activityControllers import ActivityController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllActivites():
    return ActivityController.getAllActivities()

@router.get("/{id}")
def getActivitesDetail():
    return ActivityController.getActivityDetail(id)