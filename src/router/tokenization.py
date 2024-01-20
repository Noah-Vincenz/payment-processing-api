from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.dependencies import get_tokenization_service
from src.service.tokenization import TokenizationService

router = APIRouter()


class TokenizationRequestSchema(BaseModel):
    cardholder_name: str
    card_number: str
    cvv: str
    expiry_year: str
    expiry_month: str


class TokenizationResponseSchema(BaseModel):
    token: str


@router.post("/tokens", response_model=TokenizationResponseSchema)
def tokenize(
    body: TokenizationRequestSchema,
    tokenization_service: TokenizationService = Depends(get_tokenization_service),
) -> TokenizationResponseSchema:
    token = tokenization_service.tokenize(
        cardholder_name=body.cardholder_name,
        card_number=body.card_number,
        cvv=body.cvv,
        expiry_year=body.expiry_year,
        expiry_month=body.expiry_month,
    )
    return TokenizationResponseSchema(token=token)
