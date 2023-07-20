from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company, Department, Employee, EmployeeRoles
from company.serializers import CompanySerializer, DepartmentSerializer, EmployeeRolesSerializer, EmployeeSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)

class EmployeeRolesViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRoles.objects.all()
    serializer_class = EmployeeRolesSerializer
    permission_classes = (IsAuthenticated,)




        
    