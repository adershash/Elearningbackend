from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import RegisterView,RoleInfoView,LogoutView

urlpatterns=[
    path('api/register/',RegisterView.as_view()),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('api/role-info/',RoleInfoView.as_view()),
    path('api/logout/',LogoutView.as_view())
]