from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from apps.authentication.domain.exceptions import AuthException
from apps.authentication.application.use_cases import (
    RegisterUserUseCase,
    RegisterUserDTO,
    LoginUseCase,
)
from apps.authentication.infrastructure.repositories import DjangoUserRepository
from .serializers import (
    RegisterRequestSerializer,
    LoginRequestSerializer,
    UserResponseSerializer,
)

UserModel = get_user_model()


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = RegisterUserDTO(**serializer.validated_data)
        use_case = RegisterUserUseCase(DjangoUserRepository())

        try:
            user_entity = use_case.execute(dto)
            django_user = UserModel.objects.get(pk=user_entity.id)
            token, _ = Token.objects.get_or_create(user=django_user)

            return Response({
                "message": "Usuario registrado exitosamente",
                "user": UserResponseSerializer(user_entity).data,
                "token": token.key,
            }, status=status.HTTP_201_CREATED)
        except AuthException as err:
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        use_case = LoginUseCase(DjangoUserRepository())

        try:
            user_entity = use_case.execute(
                username_or_email=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
            )
            django_user = UserModel.objects.get(pk=user_entity.id)
            token, _ = Token.objects.get_or_create(user=django_user)

            return Response({
                "message": "Inicio de sesión exitoso",
                "user": UserResponseSerializer(user_entity).data,
                "token": token.key,
            }, status=status.HTTP_200_OK)
        except AuthException as err:
            return Response({"error": str(err)}, status=status.HTTP_401_UNAUTHORIZED)


class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        repo = DjangoUserRepository()
        user_entity = repo.get_by_id(request.user.id)
        if not user_entity:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        return Response(UserResponseSerializer(user_entity).data, status=status.HTTP_200_OK)