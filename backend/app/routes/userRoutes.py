from fastapi import APIRouter, Depends
from models.userModel import User
from controllers.userControllers import UserController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllUser(db: Session):
    return UserController.getAllUser()

@router.get("/{id}")
def getUserDetail(id: int, db: Session):
    return UserController.getUserDetail(id)