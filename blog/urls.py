from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home, name='home'),
    path('create-blog/',views.Createblog, name='create-blog'),
    path('blog/<str:slug>/update/',views.Updateblog, name='update-blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)