from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Сериализуем данные
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Создаём пользователя вручную
        user = User.objects.create_user(**serializer.validated_data)

        # Генерация токенов
        refresh = RefreshToken.for_user(user)

        # Возвращаем ответ с токенами и данными пользователя
        return Response({
            'username': user.username,
            'email': user.email,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверка данных

        # Получаем пользователя из сериализатора и генерируем токены
        user = serializer.validated_data['user']
        tokens = serializer.get_tokens(user)

        return Response(tokens, status=status.HTTP_200_OK)

