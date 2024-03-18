from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    mobile_no = models.CharField(max_length=10)
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname