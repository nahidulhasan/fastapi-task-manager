from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- User schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    class Config:
        orm_mode = True

# --- Token ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- Task schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "LOW"
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskOut(TaskBase):
    id: int
    completed: bool
    owner_id: int
    created_at: datetime
    class Config:
        orm_mode = True
