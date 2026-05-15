from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers.account_router import router as account_router

from app.core.database import (
    engine,
    Base
)

from app.routers.auth_router import (
    router as auth_router
)
from app.routers.loan_router import (
    router as loan_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Banking Management System'
)

app.include_router(auth_router)
app.include_router(account_router)
app.include_router(loan_router)

@app.get('/')
def home():
    return {
        'message': 'Banking API Running Successfully'
    }