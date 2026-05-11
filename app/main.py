from fastapi import FastAPI

from app.core.database import (
    engine,
    Base
)

from app.routers.auth_router import (
    router as auth_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Banking Management System'
)

app.include_router(auth_router)

@app.get('/')
def home():
    return {
        'message': 'Banking API Running Successfully'
    }
