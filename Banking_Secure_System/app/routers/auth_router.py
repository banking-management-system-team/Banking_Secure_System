from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.schemas.auth_schema import (
    UserRegister,
    UserLogin
)

from app.services.auth_service import (
    register_service,
    login_service
)

from app.core.database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    return register_service(
        db,
        user
    )


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    return login_service(
        db,
        user
    )