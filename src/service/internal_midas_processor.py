from typing import Optional
import uuid

from src.common import AuthorizationStatus, CardDetails
from src.external.achilles_processor import ThirdPartyAchillesProcessor
from src.external.midas_processor import ThirdPartyMidasProcessor
from src.router.payments import AuthorizationResponseSchema


class InternalMidasProcessor:

    def __init__(self):
        self.midas_processor = ThirdPartyMidasProcessor()

    def send_authorisation_request(
        self,
        body,
        card_details
    ) -> AuthorizationResponseSchema:
        """
        1) send request based on processor id
        2) convert response to our model
        """
        response = self.midas_processor.auth(int(body.amount), body.currency_code, card_details.card_number, card_details.cvv)
        if response['transaction']['status'] == 'authorised':
            return AuthorizationResponseSchema(processor_transaction_id=response['transaction']['id'], status=AuthorizationStatus.AUTHORIZED)
        else:
            return AuthorizationResponseSchema(processor_transaction_id=response['transaction']['id'], status=AuthorizationStatus.DECLINED)
