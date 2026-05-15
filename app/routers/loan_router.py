from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.schemas.loan_schema import (
    LoanCreate
)

from app.services.loan_service import (
    create_loan_service,
    get_all_loans_service,
    get_loan_by_id_service,
    update_loan_service,
    delete_loan_service
)

from app.core.database import get_db

from app.utils.jwt_handler import (
    get_current_user
)

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.post("/")
def create_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        return create_loan_service(
            db,
            loan,
            current_user
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/")
def get_all_loans(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        return get_all_loans_service(db)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{loan_id}")
def get_loan_by_id(
    loan_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        return get_loan_by_id_service(
            db,
            loan_id
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.put("/{loan_id}")
def update_loan(
    loan_id: int,
    loan: LoanCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        return update_loan_service(
            db,
            loan_id,
            loan
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/{loan_id}")
def delete_loan(
    loan_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    try:

        return delete_loan_service(
            db,
            loan_id
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )