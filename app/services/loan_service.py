from sqlalchemy.orm import Session

from app.repositories.loan_repository import (
    create_loan,
    get_all_loans,
    get_loan_by_id,
    update_loan,
    delete_loan
)


def create_loan_service(
    db: Session,
    loan_data
):

    loan = create_loan(
        db,
        loan_data
    )

    return {
        "message": "Loan created successfully",
        "data": loan
    }


def get_all_loans_service(
    db: Session
):

    loans = get_all_loans(db)

    return {
        "data": loans
    }


def get_loan_by_id_service(
    db: Session,
    loan_id: int
):

    loan = get_loan_by_id(
        db,
        loan_id
    )

    if not loan:
        return {
            "message": "Loan not found"
        }

    return {
        "data": loan
    }


def update_loan_service(
    db: Session,
    loan_id: int,
    loan_data
):

    loan = update_loan(
        db,
        loan_id,
        loan_data
    )

    if not loan:
        return {
            "message": "Loan not found"
        }

    return {
        "message": "Loan updated successfully",
        "data": loan
    }


def delete_loan_service(
    db: Session,
    loan_id: int
):

    loan = delete_loan(
        db,
        loan_id
    )

    if not loan:
        return {
            "message": "Loan not found"
        }

    return {
        "message": "Loan deleted successfully"
    }