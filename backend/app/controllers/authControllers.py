from fastapi import Depends

from models.userModel import User
from sqlalchemy.orm import Session

class AuthController:
    def register(db: Session):
        return "register"
    
    def login(email: str, db: Session):
        return "login"
    
    def verify():
        return "verify"
    