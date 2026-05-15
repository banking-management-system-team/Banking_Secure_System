from fastapi import FastAPI

from app.core.database import (
    Base,
    engine
)

from app.routers.auth_router import (
    router as auth_router
)

from app.routers.account_router import (
    router as account_router
)

from app.routers.transaction_router import (
    router as transaction_router
)


# Create Database Tables
Base.metadata.create_all(bind=engine)


# FastAPI App
app = FastAPI(
    title="Banking Management System"
)


# Include Routers
app.include_router(auth_router)

app.include_router(account_router)

app.include_router(transaction_router)


# Root Endpoint
@app.get("/")
def home():

    return {
        "message": "Banking API Running Successfully"
    }