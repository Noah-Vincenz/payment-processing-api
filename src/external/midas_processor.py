from uuid import uuid4


"""
This module is "fake" and fixed as it represents a third-party processor, so you shouldn't edit it.
"""


class MissingCardDetailsException(Exception):
    ...


class ThirdPartyMidasProcessor:
    def auth(
        self, amount: int, currency_code: str, card_long_number: str, security_code: str
    ):
        if not all([card_long_number, security_code]):
            raise MissingCardDetailsException
        return {
            "transaction": {
                "id": uuid4().hex,
                "status": "authorised",
                "amount": amount,
                "currency_code": currency_code,
            },
            "card": {"last_4": card_long_number[-4:]},
        }
