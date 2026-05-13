from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.account_repository import AccountRepository
from app.schemas.account_schema import AccountCreate, AccountUpdate


class AccountService:

    @staticmethod
    def create_account(db: Session, account: AccountCreate, user_id: int):
        try:
            return AccountRepository.create_account(db, account, user_id)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Account creation failed: duplicate account number or invalid data."
            )

    @staticmethod
    def get_user_accounts(db: Session, user_id: int):
        return AccountRepository.get_user_accounts(db, user_id)

    @staticmethod
    def get_user_account_by_id(db: Session, account_id: int, user_id: int):
        return AccountRepository.get_user_account_by_id(db, account_id, user_id)

    @staticmethod
    def update_account(db: Session, account_id: int, updated_data: AccountUpdate, user_id: int):
        return AccountRepository.update_account(db, account_id, updated_data, user_id)

    @staticmethod
    def delete_account(db: Session, account_id: int, user_id: int):
        return AccountRepository.delete_account(db, account_id, user_id)
