from rest_framework import serializers
from company.models import Company, Department, Employee, EmployeeRoles

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = '__all__'

