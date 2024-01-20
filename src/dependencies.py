from functools import lru_cache
from src.service.authorization import AuthorizationService

from src.service.tokenization import TokenizationService


@lru_cache
def get_tokenization_service() -> TokenizationService:
    return TokenizationService()


@lru_cache
def get_authorization_service() -> AuthorizationService:
    return AuthorizationService()
