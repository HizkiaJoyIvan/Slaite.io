from fastapi import Depends

from models.taskModel import Task
from sqlalchemy.orm import Session

class TaskController:
    def getAllTasks(db: Session):
        # return db.query(User).all()
        return "Get All Tasks"
    
    def getTasksDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get Tasks Detail"