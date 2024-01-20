from enum import Enum

from pydantic import BaseModel


class CardDetails(BaseModel):
    cardholder_name: str
    card_number: str
    cvv: str
    expiry_year: str
    expiry_month: str


class AuthorizationStatus(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    DECLINED = "DECLINED"


class ProcessorId(str, Enum):
    ACHILLES = "ACHILLES"
    MIDAS = "MIDAS"
