from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.core.database import get_db

from app.schemas.transaction_schema import (
    DepositSchema,
    WithdrawSchema,
    TransferSchema,
    TransactionResponse
)

from app.services.transaction_service import TransactionService




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
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
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
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
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
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return TransactionService.transfer(
        db,
        current_user,
        payload.sender_account,
        payload.receiver_account,
        payload.amount
    )


@router.get(
    "/history/{account_number}"
)
def transaction_history(
    account_number: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
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
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return TransactionService.get_transaction(
        db,
        current_user,
        transaction_id
    )