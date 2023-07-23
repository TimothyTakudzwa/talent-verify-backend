from rest_framework import serializers
from company.models import Company, Department, Employee, EmployeeRoles
from user.models import User
from company.crypto import EncryptedCharField

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def validate(self, attrs):
        company = attrs.get('company')
        name = attrs.get('name').title()
        department = Department.objects.filter(name=name, company=company).first()
        if department:
            raise serializers.ValidationError("Department already exists")
        return super().validate(attrs)

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(required=False)
    id_number = serializers.CharField()
    role = serializers.CharField(required=False)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'company', 'id_number', 'date_started', 'date_ended', 'role']

    def create(self, validated_data):
        department_data = validated_data.pop('department', None)
        department_name = None
        role = validated_data.pop('role', None)
        print(validated_data)
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
        role = EmployeeRoles.objects.create(employee=employee, name=role, current=True, date_started=validated_data.get('date_started'), date_ended=validated_data.get('date_ended'))

        
        # TODO: Handle roles implementation
        return employee
    
    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        rep['company'] = instance.company.name
        rep['department'] = instance.department.name
        # g
        # print(instance.roles.all())
        try:
            rep['role'] = instance.roles.filter(current=True).first().name
        except:
            rep['role'] = "No Current Role Updated"
        return rep



class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = '__all__'
    
    def validate(self, attrs):        
        
        return super().validate(attrs)
    

