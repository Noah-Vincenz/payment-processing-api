from typing import Optional
import uuid

from src.common import AuthorizationStatus, CardDetails
from src.external.achilles_processor import ThirdPartyAchillesProcessor
from src.external.midas_processor import ThirdPartyMidasProcessor
from src.router.payments import AuthorizationRequestSchema, AuthorizationResponseSchema


class InternalAchillesProcessor:

    def __init__(self):
        self.achilles_processor = ThirdPartyAchillesProcessor()

    def send_authorisation_request(
        self,
        body,
        card_details
    ) -> AuthorizationResponseSchema :
        """
        1) send request based on processor id
        2) convert response to our model
        """
        response = self.achilles_processor.do_authorize(card_details.card_number, card_details.cvv, body.amount, body.currency_code)
        if response['auth_success']:
            return AuthorizationResponseSchema(processor_transaction_id=response['achilles_transaction_id'], status=AuthorizationStatus.AUTHORIZED)
        else:
            return AuthorizationResponseSchema(processor_transaction_id=response['achilles_transaction_id'], status=AuthorizationStatus.DECLINED)
