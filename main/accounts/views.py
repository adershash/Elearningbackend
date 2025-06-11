from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Student,Teacher,AdminProfile
from rest_framework import status,generics
from rest_framework.response import Response
from .serializer import StudentSerializer,TeacherSerializer,AdminProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        data=request.data
        role=data.get('role')
        user=User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
        if role=='student':
            Student.objects.create(user=user,name=data.get('username'))
        elif role=='teacher':
            Teacher.objects.create(user=user)
        elif role=='admin':
            AdminProfile.objects.create(user=user)
        return Response({'message':"user created successfully"},status=status.HTTP_201_CREATED)
    
class RoleInfoView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        if hasattr(user,'student'):
            return Response({'role':'student','data':StudentSerializer(user.student).data})
        elif hasattr(user,'teacher'):
            return Response({'role':'teacher','data':TeacherSerializer(user.teacher).data})
        elif hasattr(user,'adminprofile'):
            return Response({'role':'admin','data':AdminProfileSerializer(user.adiminprofile).data})
        else:
            return Response({'role':'unknown'})
        
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data['refresh']
            token=RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
