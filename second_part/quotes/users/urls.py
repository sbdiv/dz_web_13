from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('reset-password/', views.reset_password_request, name='reset-password'),
    path('reset-password/<str:token>/', views.reset_password, name='reset-password-confirm'),
]
