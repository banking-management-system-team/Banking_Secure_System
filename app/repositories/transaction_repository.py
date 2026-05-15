# app/repositories/transaction_repository.py

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.transaction_model import Transaction


class TransactionRepository:

    @staticmethod
    def create_transaction(
        db: Session,
        transaction_data: dict
    ):

        transaction = Transaction(
            **transaction_data
        )

        db.add(transaction)

        db.commit()

        db.refresh(transaction)

        return transaction

    @staticmethod
    def get_transaction_by_id(
        db: Session,
        transaction_id: int
    ):

        return (
            db.query(Transaction)
            .filter(
                Transaction.id == transaction_id
            )
            .first()
        )

    @staticmethod
    def get_transaction_history(
        db: Session,
        account_id: int
    ):

        return (
            db.query(Transaction)
            .filter(
                or_(
                    Transaction.account_id == account_id,
                    Transaction.sender_account_id == account_id,
                    Transaction.receiver_account_id == account_id
                )
            )
            .order_by(
                Transaction.id.desc()
            )
            .all()
        )