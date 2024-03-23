from fastapi import APIRouter, Depends
from controllers.taskControllers import TaskController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllTasks():
    return TaskController.getAllTasks()

@router.get("/{id}")
def getTasksDetail(id):
    return TaskController.getTasksDetail(id)