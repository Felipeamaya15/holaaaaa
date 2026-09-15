from typing import Optional
from django.contrib.auth import authenticate, get_user_model
from apps.authentication.domain.entities import UserEntity
from apps.authentication.domain.interfaces import IUserRepository

UserModel = get_user_model()


class DjangoUserRepository(IUserRepository):
    """Implementación concreta del repositorio usando Django ORM y PostgreSQL"""

    def _to_entity(self, user_obj: UserModel) -> UserEntity:
        return UserEntity(
            id=user_obj.id,
            username=user_obj.username,
            email=user_obj.email,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            is_active=user_obj.is_active,
            is_staff=user_obj.is_staff,
            date_joined=user_obj.date_joined,
        )

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        try:
            user = UserModel.objects.get(pk=user_id)
            return self._to_entity(user)
        except UserModel.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Optional[UserEntity]:
        try:
            user = UserModel.objects.get(email__iexact=email)
            return self._to_entity(user)
        except UserModel.DoesNotExist:
            return None

    def get_by_username(self, username: str) -> Optional[UserEntity]:
        try:
            user = UserModel.objects.get(username__iexact=username)
            return self._to_entity(user)
        except UserModel.DoesNotExist:
            return None

    def create(self, user: UserEntity, password: str) -> UserEntity:
        user_record = UserModel.objects.create_user(
            username=user.username,
            email=user.email,
            password=password,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        return self._to_entity(user_record)

    def verify_credentials(self, username_or_email: str, password: str) -> Optional[UserEntity]:
        user = authenticate(username=username_or_email, password=password)
        
        # Si no autenticó por username, intentamos por email
        if not user and '@' in username_or_email:
            try:
                user_found = UserModel.objects.get(email__iexact=username_or_email)
                user = authenticate(username=user_found.username, password=password)
            except UserModel.DoesNotExist:
                return None

        if user and user.is_active:
            return self._to_entity(user)
        return None