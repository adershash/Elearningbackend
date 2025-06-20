from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='profileimage/',null=True)
    bio=models.TextField(max_length=500,null=True)

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    about=models.TextField(max_length=500,null=True)
    image=models.ImageField(upload_to='profileimage/',null=True)
    

class AdminProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='profileimage/',null=True)

    
