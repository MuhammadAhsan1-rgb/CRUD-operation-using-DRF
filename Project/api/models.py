from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department,  on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name