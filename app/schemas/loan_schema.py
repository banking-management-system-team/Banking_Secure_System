from pydantic import BaseModel


class LoanCreate(BaseModel):

    account_id: int
    loan_type: str
    amount: float
    interest_rate: float
    duration_months: int


class LoanResponse(BaseModel):

    id: int
    account_id: int
    loan_type: str
    amount: float
    interest_rate: float
    duration_months: int
    status: str

    class Config:
        from_attributes = True