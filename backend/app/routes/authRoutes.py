from fastapi import APIRouter, status, HTTPException
from controllers.authControllers import AuthController

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(res):
    return AuthController.login()

@router.post("/register")
def register(res):
    return AuthController.register()

@router.post("/verify")
def verify(res):
    return AuthController.verify()