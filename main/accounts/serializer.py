from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student,Teacher,AdminProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Student
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Teacher
        fields='__all__'

class AdminProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=AdminProfile
        fields='__all__'