from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signupView,name='signup'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('forgotpassword/',views.forgotPassword,name='forgotpassword'),
    path('adminDashboard/',views.adminDashboard,name='adminDashboard'),
    path('userDashboard/',views.index,name='userDashboard')
]