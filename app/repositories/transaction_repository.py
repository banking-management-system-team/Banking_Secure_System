from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.transaction_model import Transaction


class TransactionRepository:

    @staticmethod
    def create_transaction(db: Session, transaction_data: dict):

        transaction = Transaction(**transaction_data)

        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        return transaction

    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: int):

        return (
            db.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

    @staticmethod
    def get_transaction_history(db: Session, account_number: str):

        return (
            db.query(Transaction)
            .filter(
                or_(
                    Transaction.sender_account == account_number,
                    Transaction.receiver_account == account_number
                )
            )
            .order_by(Transaction.id.desc())
            .all()
        )