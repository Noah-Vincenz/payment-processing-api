from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.common import AuthorizationStatus, ProcessorId
from src.dependencies import get_authorization_service, get_tokenization_service
from src.external.achilles_processor import ThirdPartyAchillesProcessor
from src.external.midas_processor import ThirdPartyMidasProcessor
from src.service.authorization import AuthorizationService
from src.service.tokenization import TokenizationService

router = APIRouter()

processor_id_to_service_dict = {ProcessorId.ACHILLES: InternalAchillesProcessor(), ProcessorId.MIDAS: InternalMidasProcessor()}

class AuthorizationRequestSchema(BaseModel):
    token: str
    processor_id: ProcessorId
    amount: str
    currency_code: str


class AuthorizationResponseSchema(BaseModel):
    processor_transaction_id: str
    status: AuthorizationStatus


@router.post("/payments", response_model=AuthorizationResponseSchema)
def authorize_payment(
    body: AuthorizationRequestSchema,
    tokenization_service: TokenizationService = Depends(get_tokenization_service),
    authorization_service: AuthorizationService = Depends(get_authorization_service),
) -> AuthorizationResponseSchema:
    """
    1) get CardDetails from dict
    2) check if exists
    3) create request for specific third party processor
    4) return authorisation response based on external party response
    """
    card_details = tokenization_service.detokenize(body.token)
    # check if token exists in dict
    if card_details != None:
        third_party_processor = body.processor_id
        previous_amount = body.amount
        body.amount = previous_amount * 100 # to move away from minor units
        internal_processor = processor_id_to_service_dict[third_party_processor]
        internal_processor.send_authorisation_request(body, card_details)
        response = authorization_service.send_authorisation_request(third_party_processor)
        # convert into AuthorizationResponseSchema
