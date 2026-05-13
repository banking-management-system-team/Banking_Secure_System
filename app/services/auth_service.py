from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.auth_repository import (
    get_user_by_email,
    create_user
)

from app.utils.password import (
    hash_password,
    verify_password
)

from app.core.security import (
    create_access_token
)


def register_service(
    db: Session,
    user_data
):

    try:
        existing_user = get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            return {
                "message": "Email already registered",
                "status": "error"
            }

        hashed_password = hash_password(
            user_data.password
        )

        create_user(
            db,
            user_data.full_name,
            user_data.email,
            hashed_password
        )

        return {
            "message": "User Registered Successfully",
            "status": "success"
        }
    except IntegrityError as e:
        db.rollback()
        return {
            "message": "Email already exists",
            "status": "error"
        }
    except Exception as e:
        db.rollback()
        raise Exception(f"Registration error: {str(e)}")


def login_service(
    db: Session,
    user_data
):

    try:
        user = get_user_by_email(
            db,
            user_data.email
        )

        if not user:
            return {
                "message": "Invalid Email",
                "status": "error"
            }

        password_check = verify_password(
            user_data.password,
            user.password
        )

        if not password_check:
            return {
                "message": "Invalid Password",
                "status": "error"
            }

        token = create_access_token(
            data={
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "status": "success"
        }
    except Exception as e:
        raise Exception(f"Login error: {str(e)}")