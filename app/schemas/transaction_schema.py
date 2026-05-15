from pydantic import BaseModel
from datetime import datetime


class DepositSchema(BaseModel):

    account_number: str
    amount: float


class WithdrawSchema(BaseModel):

    account_number: str
    amount: float


class TransferSchema(BaseModel):

    sender_account_number: str
    receiver_account_number: str
    amount: float


class TransactionResponse(BaseModel):

    id: int

    # Deposit & Withdraw
    account_id: int | None = None

    # Transfer
    sender_account_id: int | None = None

    receiver_account_id: int | None = None

    amount: float

    transaction_type: str

    status: str

    description: str | None = None

    created_at: datetime

    class Config:

        from_attributes = True