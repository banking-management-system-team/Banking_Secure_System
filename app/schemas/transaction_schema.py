from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DepositSchema(BaseModel):
    account_number: str
    amount: float

    class Config:
        from_attributes = True


class WithdrawSchema(BaseModel):
    account_number: str
    amount: float

    class Config:
        from_attributes = True


class TransferSchema(BaseModel):
    sender_account: str
    receiver_account: str
    amount: float

    class Config:
        from_attributes = True


class TransactionResponse(BaseModel):
    id: int
    sender_account: Optional[str]
    receiver_account: Optional[str]
    amount: float
    transaction_type: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True