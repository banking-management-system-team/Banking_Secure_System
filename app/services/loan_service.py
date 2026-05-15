from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.models.account_model import Account

from app.repositories.loan_repository import (
    create_loan,
    get_all_loans,
    get_loan_by_id,
    update_loan,
    delete_loan
)


def create_loan_service(
    db: Session,
    loan_data,
    current_user
):

    account = db.query(Account).filter(
        Account.id == loan_data.account_id
    ).first()

    # Account not found
    if not account:

        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    # Another user's account
    if account.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="You cannot use another user's account"
        )

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