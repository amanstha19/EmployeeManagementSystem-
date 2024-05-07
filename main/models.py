from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=10)

