from fastapi import Depends

from models.userModel import User
from sqlalchemy.orm import Session

class UserController:
    def getAllUser(db: Session):
        # return db.query(User).all()
        return "Get All User"
    
    def getUserDetail(email: str, db: Session):
        # return db.query(User).filter(User.email == email).first()
        return "Get User Detail"