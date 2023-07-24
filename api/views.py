from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from api.serializers import AuthTokenObtainPairSerializer

class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer