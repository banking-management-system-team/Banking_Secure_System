from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.transaction_repository import TransactionRepository
from app.repositories.account_repository import AccountRepository

from app.models.user_model import User


class TransactionService:

    @staticmethod
    def deposit(
        db: Session,
        user: User,
        account_number: str,
        amount: float
    ):

        account = (
            AccountRepository.get_account_by_number(
                db,
                account_number
            )
        )

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        # Logged-in user can use only own account
        if account.user_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        account.balance += amount

        AccountRepository.update_account_balance(
            db,
            account
        )

        transaction_data = {

            "account_id": account.id,

            "amount": amount,

            "transaction_type": "DEPOSIT",

            "status": "SUCCESS"
        }

        return TransactionRepository.create_transaction(
            db,
            transaction_data
        )

    @staticmethod
    def withdraw(
        db: Session,
        user: User,
        account_number: str,
        amount: float
    ):

        account = (
            AccountRepository.get_account_by_number(
                db,
                account_number
            )
        )

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        # Logged-in user can use only own account
        if account.user_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        if account.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        account.balance -= amount

        AccountRepository.update_account_balance(
            db,
            account
        )

        transaction_data = {

            "account_id": account.id,

            "amount": amount,

            "transaction_type": "WITHDRAW",

            "status": "SUCCESS"
        }

        return TransactionRepository.create_transaction(
            db,
            transaction_data
        )

    @staticmethod
    def transfer(
        db: Session,
        user: User,
        sender_account_number: str,
        receiver_account_number: str,
        amount: float
    ):

        sender_account = (
            AccountRepository.get_account_by_number(
                db,
                sender_account_number
            )
        )

        receiver_account = (
            AccountRepository.get_account_by_number(
                db,
                receiver_account_number
            )
        )

        if not sender_account:
            raise HTTPException(
                status_code=404,
                detail="Sender account not found"
            )

        if not receiver_account:
            raise HTTPException(
                status_code=404,
                detail="Receiver account not found"
            )

        # Logged-in user can transfer only from own account
        if sender_account.user_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        if sender_account.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        sender_account.balance -= amount

        receiver_account.balance += amount

        AccountRepository.update_account_balance(
            db,
            sender_account
        )

        AccountRepository.update_account_balance(
            db,
            receiver_account
        )

        transaction_data = {

            "sender_account_id": sender_account.id,

            "receiver_account_id": receiver_account.id,

            "amount": amount,

            "transaction_type": "TRANSFER",

            "status": "SUCCESS"
        }

        return TransactionRepository.create_transaction(
            db,
            transaction_data
        )

    @staticmethod
    def get_transaction(
        db: Session,
        transaction_id: int
    ):

        transaction = (
            TransactionRepository.get_transaction_by_id(
                db,
                transaction_id
            )
        )

        if not transaction:
            raise HTTPException(
                status_code=404,
                detail="Transaction not found"
            )

        return transaction

    @staticmethod
    def get_history(
        db: Session,
        user: User,
        account_number: str
    ):

        account = (
            AccountRepository.get_account_by_number(
                db,
                account_number
            )
        )

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        if account.user_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        return TransactionRepository.get_transaction_history(
            db,
            account.id
        )