from django.shortcuts import render
from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import isOwnerOrSuperUser

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()