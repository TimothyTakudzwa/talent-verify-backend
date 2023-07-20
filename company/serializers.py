from rest_framework import serializers
from company.models import Company, Department, Employee, EmployeeRoles

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(required=False)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        department_data = validated_data.pop('department', None)
        department_name = None

        if department_data:
            department_name = department_data.get('name').title()
            department = Department.objects.filter(name=department_name).first()

            if not department:
                # Create a new department if it doesn't exist
                department = Department.objects.create(name=department_name.title(), company=validated_data.get('company'))

            # Attach the department object to the validated data
            validated_data['department'] = department

        # Create the Employee instance with the updated validated data
        employee = Employee.objects.create(**validated_data)
        return employee


class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = '__all__'
    
    def validate(self, attrs):        
        
        return super().validate(attrs)
