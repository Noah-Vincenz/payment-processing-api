from uuid import uuid4


"""
This module is "fake" and fixed as it represents a third-party processor, so you shouldn't edit it.
"""


class MissingCardDetailsException(Exception):
    ...


class ThirdPartyAchillesProcessor:
    def do_authorize(self, card_number: str, cvc: str, amount: str, currency_code: str):
        if not all([card_number, cvc]):
            raise MissingCardDetailsException

        return {
            "achilles_transaction_id": uuid4().hex,
            "auth_success": False,
            "last_4": card_number[-4:],
            "amount": amount,
            "currency_code": currency_code,
        }
