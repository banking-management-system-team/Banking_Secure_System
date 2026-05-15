from sqlalchemy.orm import Session

from app.models.loan_model import Loan


def create_loan(
    db: Session,
    loan_data
):

    new_loan = Loan(
        account_id=loan_data.account_id,
        loan_type=loan_data.loan_type,
        amount=loan_data.amount,
        interest_rate=loan_data.interest_rate,
        duration_months=loan_data.duration_months
    )

    db.add(new_loan)

    db.commit()

    db.refresh(new_loan)

    return new_loan


def get_all_loans(db: Session):

    return db.query(Loan).all()


def get_loan_by_id(
    db: Session,
    loan_id: int
):

    return db.query(Loan).filter(
        Loan.id == loan_id
    ).first()


def update_loan(
    db: Session,
    loan_id: int,
    loan_data
):

    loan = db.query(Loan).filter(
        Loan.id == loan_id
    ).first()

    if not loan:
        return None

    loan.loan_type = loan_data.loan_type
    loan.amount = loan_data.amount
    loan.interest_rate = loan_data.interest_rate
    loan.duration_months = loan_data.duration_months

    db.commit()

    db.refresh(loan)

    return loan


def delete_loan(
    db: Session,
    loan_id: int
):

    loan = db.query(Loan).filter(
        Loan.id == loan_id
    ).first()

    if not loan:
        return None

    db.delete(loan)

    db.commit()

    return loan