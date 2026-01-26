from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import RegisterRequest, LoginRequest
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    truncated_password = password[:72]
    return pwd_context.hash(truncated_password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password[:72], hashed_password)


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = f"fake-token-for-{user.id}"
    return {"access_token": token, "token_type": "bearer"}





@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # HASH PASSWORD
    hashed_pwd = hash_password(request.password)

    new_user = User(email=request.email, password=hashed_pwd, full_name=request.full_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.id}
class UpdateUserRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: Optional[str] = None  # Optional for updates

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "full_name": u.full_name, "email": u.email} for u in users]

@router.get("/users/{user_id}")
def get_user(user_id: int, current_user: dict = Depends(current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "full_name": user.full_name, "email": user.email}

@router.patch("/users/{user_id}")
def update_user(user_id: int, update_data: UpdateUserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.full_name = update_data.full_name
    user.email = update_data.email
    if update_data.password:
        user.password = hash_password(update_data.password)

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": {"id": user.id, "full_name": user.full_name, "email": user.email}}

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}