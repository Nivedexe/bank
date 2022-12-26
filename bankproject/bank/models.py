
from django.db import models
#  gpyt



class MyModel(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    email = models.EmailField(null=True)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account=models.CharField(max_length=20,null=True)
    materials=models.TextField()


