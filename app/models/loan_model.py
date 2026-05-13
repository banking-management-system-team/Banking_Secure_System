from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from app.core.database import Base


class Loan(Base):

    __tablename__ = "loans"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    loan_type = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    interest_rate = Column(
        Float,
        nullable=False
    )

    duration_months = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String,
        default="Pending"
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    user = relationship("User")