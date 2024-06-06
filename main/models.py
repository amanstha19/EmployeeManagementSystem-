from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50, primary_key=True)  
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    working_part = models.BooleanField(default=True)
     
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50, primary_key=True)  
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    working = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class OfficeHead(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50, primary_key=True)  #
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    working = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Onleave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_start = models.DateField()
    leave_end = models.DateField()

class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField()
