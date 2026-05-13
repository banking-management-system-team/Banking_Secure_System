from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.core.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_account = Column(String, nullable=True)
    receiver_account = Column(String, nullable=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)
    status = Column(String, default="SUCCESS")
    created_at = Column(DateTime, default=datetime.utcnow)