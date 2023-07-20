from django.db import models

from company.crypto import EncryptedCharField

class Company(models.Model):
    """
    Model for employers who will upload their employees
    """

    name = models.CharField(max_length=100)
    registration_number = EncryptedCharField(max_length=100)
    date_of_registration = models.DateField()
    address = models.CharField(max_length=100)
    contact_person = EncryptedCharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Companies'


class Department(models.Model):
    """
    Model for departments in a company
    """

    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Departments'


class Employee(models.Model):
    """
    Model for employees in a company
    """

    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=100)
    id_number = EncryptedCharField(max_length=100)
    date_started = models.DateField()
    date_ended = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Employees'

class EmployeeRoles(models.Model):
    """
    Model for roles of employees
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='roles')
    name = models.CharField(max_length=100)
    date_started = models.DateField()
    date_ended = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Employee Roles'

class RoleDuties(models.Model):
    """
    Model for duties of roles
    """

    role = models.ForeignKey(EmployeeRoles, on_delete=models.CASCADE, related_name='duties')
    duty = models.CharField(max_length=500)

    def __str__(self):
        return self.duty
    
    class Meta:
        verbose_name_plural = 'Role Duties'


class EmploymentHistory(models.Model):
    """
    Model for employment history of employees
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employment_history')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employment_history')
    date_started = models.DateField()
    date_ended = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.company
    
    class Meta:
        verbose_name_plural = 'Employment History'

   