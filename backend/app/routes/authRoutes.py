from fastapi import APIRouter, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from dto.userObjects import LoginUserBody, RegisterUserBody
from models.userModel import User
from sqlalchemy.orm import Session
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(tags=["Authentication"])

@router.post("/register")
def register(body: RegisterUserBody, db: Session):
    pwd_context = CryptContext(schemes=["bcrypt"])
    existing_user = db.query(User).filter(User.email == body.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = pwd_context.hash(body.password)
    new_user = User(
        username = body.username,
        email = body.email,
        password = hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "status": "success",
        "data": new_user
    }

@router.post("/login")
def login(body: LoginUserBody, db: Session):
    pwd_context = CryptContext(schemes=["bcrypt"])
    existing_user = db.query(User).filter(User.email == body.email).first()

    if not existing_user or not pwd_context.verify(body.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    payload = {
        "email": body.email,
        "exp": datetime.now() + timedelta(hours=1)
    }
    token = jwt.encode(payload, 'SECRET', algorithm='HS256')
    return {
        "status": "success",
        "token": token
    }

@router.post("/verify")
def verify(res):
    return "Verify"