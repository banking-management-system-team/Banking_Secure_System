from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class AccountCreate(BaseModel):
    account_holder_name: str
    email: EmailStr
    phone: str
    account_number: str
    account_type: str
    branch: str
    ifsc_code: str
    balance: float


class AccountResponse(BaseModel):
    id: int
    account_holder_name: str
    email: EmailStr
    phone: str
    account_number: str
    account_type: str
    branch: str
    ifsc_code: str
    balance: float
    status: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AccountUpdate(BaseModel):
    account_holder_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    account_type: Optional[str] = None
    branch: Optional[str] = None
    ifsc_code: Optional[str] = None
    balance: Optional[float] = None
    status: Optional[str] = None