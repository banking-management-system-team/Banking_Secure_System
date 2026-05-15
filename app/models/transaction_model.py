# app/models/transaction_model.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from app.core.database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # For Deposit & Withdraw
    account_id = Column(
        Integer,
        ForeignKey("accounts.id"),
        nullable=True
    )

    # For Transfer
    sender_account_id = Column(
        Integer,
        ForeignKey("accounts.id"),
        nullable=True
    )

    receiver_account_id = Column(
        Integer,
        ForeignKey("accounts.id"),
        nullable=True
    )

    amount = Column(
        Float,
        nullable=False
    )

    transaction_type = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="SUCCESS"
    )

    description = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )