from fastapi import FastAPI
from src.router.payments import router as payments_router
from src.router.tokenization import router as tokenization_router

app = FastAPI()

app.include_router(tokenization_router)
app.include_router(payments_router)
