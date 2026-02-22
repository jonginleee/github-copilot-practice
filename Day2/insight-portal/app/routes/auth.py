"""회원가입 API"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, field_validator
import re
from app.storage import get_user_by_email, create_user
from app.security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterResponse(BaseModel):
    ok: bool
    user: dict

class ErrorResponse(BaseModel):
    ok: bool
    error_code: str
    message: str

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
def register(req: RegisterRequest):
    """회원가입
    
    - 이메일 형식 검증 (자동 - EmailStr)
    - 비밀번호 강도 검증 (8자 이상, 영문+숫자 포함)
    - 중복 이메일 체크
    """
    # 비밀번호 강도 검증
    if len(req.password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"ok": False, "error_code": "WEAK_PASSWORD", "message": "비밀번호는 8자 이상이어야 합니다"}
        )
    
    if not re.search(r'[A-Za-z]', req.password) or not re.search(r'\d', req.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"ok": False, "error_code": "WEAK_PASSWORD", "message": "비밀번호는 영문과 숫자를 포함해야 합니다"}
        )
    
    # 중복 체크
    if get_user_by_email(req.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"ok": False, "error_code": "DUPLICATE_EMAIL", "message": "이미 등록된 이메일입니다"}
        )
    
    # 사용자 생성
    hashed_pwd = hash_password(req.password)
    user = create_user(req.email, hashed_pwd)
    
    return {
        "ok": True,
        "user": {
            "id": user['id'],
            "email": user['email']
        }
    }
