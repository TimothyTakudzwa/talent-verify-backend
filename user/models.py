from django.db import models
from django.contrib.auth.models import AbstractUser

from company.models import Company

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Users'
