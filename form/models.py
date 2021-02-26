from django.db import models

# Create your models here.
GENDER=[{'m','MALE'},{'f','FEMALE'}]
STATUS=[{'0','INACTIVE'},{'1','ACTIVE'}]
class Student (models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    gender=models.CharField(choices=GENDER,max_length=50)
    status=models.CharField(choices=STATUS,max_length=50)