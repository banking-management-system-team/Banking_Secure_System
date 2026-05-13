from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from app.core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    account_holder_name = Column(String, nullable=False)

    email = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    account_number = Column(String, unique=True, nullable=False)

    account_type = Column(String, nullable=False)

    branch = Column(String, nullable=False)

    ifsc_code = Column(String, nullable=False)

    balance = Column(Float, default=0)
    status = Column(String, default="Active")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)