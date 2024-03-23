from fastapi import APIRouter, Depends
from controllers.eventControllers import EventController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllEvents():
    return EventController.getAllEvents()

@router.get("/{id}")
def getEventDetail():
    return EventController.getEventDetail(id)