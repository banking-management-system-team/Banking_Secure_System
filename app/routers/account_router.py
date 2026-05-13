from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user_model import User
from app.schemas.account_schema import (
    AccountCreate,
    AccountResponse,
    AccountUpdate
)

from app.services.account_service import AccountService

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post(
    "/create",
    response_model=AccountResponse
)
def create_account(
    account: AccountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return AccountService.create_account(db, account, current_user.id)


@router.get(
    "/",
    response_model=List[AccountResponse]
)
def get_all_accounts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return AccountService.get_user_accounts(db, current_user.id)


@router.get(
    "/{account_id}",
    response_model=AccountResponse
)
def get_account_by_id(
    account_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    account = AccountService.get_user_account_by_id(
        db,
        account_id,
        current_user.id
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found"
        )

    return account


@router.put(
    "/update/{account_id}",
    response_model=AccountResponse
)
def update_account(
    account_id: int,
    updated_data: AccountUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    account = AccountService.update_account(
        db,
        account_id,
        updated_data,
        current_user.id
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found"
        )
    return account


@router.delete(
    "/delete/{account_id}"
)
def delete_account(
    account_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = AccountService.delete_account(
        db,
        account_id,
        current_user.id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found"
        )

    return {
        "message": "Account Deleted Successfully"
    }    