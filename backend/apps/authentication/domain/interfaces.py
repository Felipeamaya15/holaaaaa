from abc import ABC, abstractmethod
from typing import Optional
from .entities import UserEntity


class IUserRepository(ABC):
    """Contrato que debe cumplir cualquier adaptador de persistencia (Postgres/Mongo)"""

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def create(self, user: UserEntity, password: str) -> UserEntity:
        pass

    @abstractmethod
    def verify_credentials(self, username_or_email: str, password: str) -> Optional[UserEntity]:
        pass