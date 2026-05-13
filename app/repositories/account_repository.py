from sqlalchemy.orm import Session

from app.models.account_model import Account
from app.schemas.account_schema import AccountCreate, AccountUpdate


class AccountRepository:

    @staticmethod
    def create_account(db: Session, account: AccountCreate, user_id: int):

        new_account = Account(
            account_holder_name=account.account_holder_name,
            email=account.email,
            phone=account.phone,
            account_number=account.account_number,
            account_type=account.account_type,
            branch=account.branch,
            ifsc_code=account.ifsc_code,
            balance=account.balance,
            user_id=user_id
        )

        db.add(new_account)
        db.commit()
        db.refresh(new_account)

        return new_account

    @staticmethod
    def get_user_accounts(db: Session, user_id: int):
        return db.query(Account).filter(Account.user_id == user_id).all()

    @staticmethod
    def get_user_account_by_id(db: Session, account_id: int, user_id: int):
        return db.query(Account).filter(
            Account.id == account_id,
            Account.user_id == user_id
        ).first()

    @staticmethod
    def update_account(db: Session, account_id: int, updated_data: AccountUpdate, user_id: int):

        account = db.query(Account).filter(
            Account.id == account_id,
            Account.user_id == user_id
        ).first()
        if not account:
            return None

        update_data = updated_data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(account, key, value)

        db.commit()
        db.refresh(account)

        return account

    @staticmethod
    def delete_account(db: Session, account_id: int, user_id: int):

        account = db.query(Account).filter(
            Account.id == account_id,
            Account.user_id == user_id
        ).first()

        if not account:
            return None
        db.delete(account)
        db.commit()

        return True    