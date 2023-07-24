import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from company.models import Company, Department, Employee, EmployeeRoles
from company.serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, EmployeeRolesSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def company_data():
    return {
        "name": "Test Company",
        "location": "Test Location",
        
    }

@pytest.fixture
def department_data():
    return {
        "name": "Test Department",
        
    }

@pytest.fixture
def employee_data(company_data, department_data):
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "company": Company.objects.create(**company_data),
        "department": Department.objects.create(**department_data),
        
    }

@pytest.fixture
def employee_roles_data():
    return {
        "role_name": "Test Role",
        
    }

@pytest.mark.django_db
class TestCompanyViewSet:

    def test_create_company(self, api_client, company_data):
        url = '/api/companies/'
        response = api_client.post(url, company_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Company.objects.filter(name=company_data['name']).exists()

    def test_retrieve_company(self, api_client, company_data):
        company = Company.objects.create(**company_data)
        url = f'/api/companies/{company.id}/'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == CompanySerializer(company).data

    


@pytest.mark.django_db
class TestEmployeeViewSet:

    def test_create_employee(self, api_client, employee_data):
        url = '/api/employees/'
        response = api_client.post(url, employee_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Employee.objects.filter(first_name=employee_data['first_name']).exists()

    def test_retrieve_employee(self, api_client, employee_data):
        employee = Employee.objects.create(**employee_data)
        url = f'/api/employees/{employee.id}/'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == EmployeeSerializer(employee).data

    # Add other EmployeeViewSet test cases as needed


@pytest.mark.django_db
class TestDepartmentViewSet:

    def test_create_department(self, api_client, department_data):
        url = '/api/departments/'
        response = api_client.post(url, department_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Department.objects.filter(name=department_data['name']).exists()

    def test_retrieve_department(self, api_client, department_data):
        department = Department.objects.create(**department_data)
        url = f'/api/departments/{department.id}/'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == DepartmentSerializer(department).data

    # Add other DepartmentViewSet test cases as needed


@pytest.mark.django_db
class TestEmployeeRolesViewSet:

    def test_create_employee_roles(self, api_client, employee_roles_data):
        url = '/api/employee-roles/'
        response = api_client.post(url, employee_roles_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert EmployeeRoles.objects.filter(role_name=employee_roles_data['role_name']).exists()

    def test_retrieve_employee_roles(self, api_client, employee_roles_data):
        employee_roles = EmployeeRoles.objects.create(**employee_roles_data)
        url = f'/api/employee-roles/{employee_roles.id}/'
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == EmployeeRolesSerializer(employee_roles).data

    # Add other EmployeeRolesViewSet test cases as needed

# Add more test cases as necessary for other views or edge cases.
