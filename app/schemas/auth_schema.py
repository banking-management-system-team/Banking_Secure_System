from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import field_validator


class UserRegister(BaseModel):

    full_name: str
    email: EmailStr
    password: str

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v):

        if len(v.strip()) < 2:
            raise ValueError(
                "Full name must be at least 2 characters long"
            )

        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):

        if len(v) < 8:
            raise ValueError(
                "Password must be at least 8 characters long"
            )

        return v


class UserLogin(BaseModel):

    email: EmailStr
    password: str