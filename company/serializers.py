from rest_framework import serializers
from company.models import Company, Department, Employee, EmployeeRoles, RoleDuties
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
        return attrs

class EmployeeRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRoles
        fields = '__all__'
    
    def validate(self, attrs):
        return attrs

class EmployeeSerializer(serializers.ModelSerializer):
    id_number = serializers.CharField()
    role = serializers.CharField(required=False)
    duties = serializers.CharField(required=False)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'company', 'id_number', 'date_started', 'date_ended', 'role', 'duties']

    def create(self, validated_data):
        department_data = validated_data.pop('department', None)
        department_name = None
        role = validated_data.pop('role', None)

        if department_data:
            department_name = department_data.name.title()
            department, _ = Department.objects.get_or_create(name=department_name.title(), company=validated_data.get('company'))

            validated_data['department'] = department
        duties = validated_data.pop('duties', None)
        employee = Employee.objects.create(**validated_data)
        
        role = EmployeeRoles.objects.create(
            employee=employee,
            name=role,
            current=True,
            date_started=validated_data.get('date_started'),
            date_ended=validated_data.get('date_ended'),
            company=validated_data.get('company')
        )
        # Duties
        duty = RoleDuties.objects.create(role=role, duties=duties)

        # TODO: Handle roles implementation
        return employee
    
    # def update(self, instance, validated_data):
        
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['company'] = instance.company.name
        rep['department'] = instance.department.name

        try:
            # Fix logic here
            current_role = instance.roles.filter(current=True).first()
            rep['role'] = current_role.name
            rep['duties'] = current_role.duties.first().duties
        except AttributeError:
            rep['role'] = ""
            rep['duties'] = ""
        return rep
    

