from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company, Department, Employee, EmployeeRoles
from company.serializers import CompanySerializer, DepartmentSerializer, EmployeeRolesSerializer, EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from user.models import User

from user.permissions import isOwnerOrSuperUser

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, isOwnerOrSuperUser) 

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, isOwnerOrSuperUser)

    def get_queryset(self):
        return super().get_queryset().filter(company=self.request.user.company)

    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,isOwnerOrSuperUser)

    def get_queryset(self):
        return super().get_queryset().filter(company=self.request.user.company)

class EmployeeRolesViewSet(viewsets.ModelViewSet, isOwnerOrSuperUser):
    queryset = EmployeeRoles.objects.all()
    serializer_class = EmployeeRolesSerializer
    permission_classes = (IsAuthenticated,)

    






        
    