from django.db import models

# Create your models here.

class EmpModels(models.Model):
    employee_name=models.CharField(max_length=120,unique=True)
    designation=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):  # THIS IS AN INSTANT METHOD
        return self.employee_name

