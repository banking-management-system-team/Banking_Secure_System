# app/routers/transaction_router.py

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user_model import User

from app.schemas.transaction_schema import (
    DepositSchema,
    WithdrawSchema,
    TransferSchema,
    TransactionResponse
)

from app.services.transaction_service import (
    TransactionService
)


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post(
    "/deposit",
    response_model=TransactionResponse
)
def deposit_money(
    payload: DepositSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return TransactionService.deposit(
        db,
        current_user,
        payload.account_number,
        payload.amount
    )


@router.post(
    "/withdraw",
    response_model=TransactionResponse
)
def withdraw_money(
    payload: WithdrawSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return TransactionService.withdraw(
        db,
        current_user,
        payload.account_number,
        payload.amount
    )


@router.post(
    "/transfer",
    response_model=TransactionResponse
)
def transfer_money(
    payload: TransferSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return TransactionService.transfer(
        db,
        current_user,
        payload.sender_account_number,
        payload.receiver_account_number,
        payload.amount
    )


@router.get(
    "/history/{account_number}"
)
def transaction_history(
    account_number: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return TransactionService.get_history(
        db,
        current_user,
        account_number
    )


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def transaction_details(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return TransactionService.get_transaction(
        db,
        transaction_id
    )