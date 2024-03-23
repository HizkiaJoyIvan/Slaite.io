from fastapi import APIRouter, Depends
from models.userModel import User
from controllers.userControllers import UserController
from sqlalchemy.orm import Session

router = APIRouter(tags=["Users"])

@router.get("/")
def getAllUser():
    return UserController.getAllUser()

@router.get("/{id}")
def getUserDetail():
    return UserController.getUserDetail(id)