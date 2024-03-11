from fastapi import APIRouter, status, HTTPException

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(res):
    return res