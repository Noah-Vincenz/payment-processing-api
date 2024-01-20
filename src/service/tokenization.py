from typing import Optional
import uuid

from src.common import CardDetails


class TokenizationService:
    def __init__(self):
        self.store: dict[str, CardDetails] = dict()

    def tokenize(
        self,
        cardholder_name: str,
        card_number: str,
        cvv: str,
        expiry_year: str,
        expiry_month: str,
    ) -> str:
        """
        1) generate token
        2) store token->CardDetails in dict
        3) return token
        """
        token = str(uuid.uuid4())
        self.store[token] = CardDetails(cardholder_name=cardholder_name, card_number=card_number, cvv=cvv, expiry_year=expiry_year, expiry_month=expiry_month)
        return token

    def detokenize(self, token: str) -> Optional[CardDetails]:
        return self.store.get(token)
