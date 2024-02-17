from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('create-blog/',views.Createblog, name='create-blog'),
]