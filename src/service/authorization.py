from typing import Optional
import uuid

from src.common import CardDetails
from src.external.achilles_processor import ThirdPartyAchillesProcessor
from src.external.midas_processor import ThirdPartyMidasProcessor


class AuthorizationService:

    def __init__(self):
        self.achilles_processor = ThirdPartyAchillesProcessor()
        self.midas_process = ThirdPartyMidasProcessor()

    def send_authorisation_request(
        self,
        processor_id
    ) -> str:
        """
        1) send request based on processor id
        """
        token = str(uuid.uuid4())
        self.store[token] = CardDetails(cardholder_name=cardholder_name, card_number=card_number, cvv=cvv, expiry_year=expiry_year, expiry_month=expiry_month)
        return token
