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
        receiver_account = AccountRepository.get_account_by_number(
            db,
            account_number
        )
        print(f"Depositing {amount} to account: {account_number} for user: {user.email}")
        print(f"Receiver account details: {receiver_account}")

        if not receiver_account:
            raise HTTPException(
                status_code=404,
                detail="Receiver account not found"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        receiver_account.balance += amount
        AccountRepository.update_account_balance(db, receiver_account)

        transaction_data = {
            "receiver_account": account_number,
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
        sender_account = AccountRepository.get_account_by_number(
            db,
            account_number
        )

        if not sender_account:
            raise HTTPException(
                status_code=404,
                detail="Sender account not found"
            )

        if sender_account.email != user.email:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to withdraw from this account"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        if sender_account.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient account balance"
            )

        sender_account.balance -= amount
        AccountRepository.update_account_balance(db, sender_account)

        transaction_data = {
            "sender_account": account_number,
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
        sender_account: str,
        receiver_account: str,
        amount: float
    ):
        sender = AccountRepository.get_account_by_number(
            db,
            sender_account
        )
        receiver = AccountRepository.get_account_by_number(
            db,
            receiver_account
        )

        if not sender:
            raise HTTPException(
                status_code=404,
                detail="Sender account not found"
            )

        if not receiver:
            raise HTTPException(
                status_code=404,
                detail="Receiver account not found"
            )

        if sender.email != user.email:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to transfer from this account"
            )

        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Amount must be greater than zero"
            )

        if sender.balance < amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient account balance"
            )

        sender.balance -= amount
        receiver.balance += amount

        AccountRepository.update_account_balance(db, sender)
        AccountRepository.update_account_balance(db, receiver)

        transaction_data = {
            "sender_account": sender_account,
            "receiver_account": receiver_account,
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
        user: User,
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
        return (
            TransactionRepository.get_transaction_history(
                db,
                account_number
            )
        )