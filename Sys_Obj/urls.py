from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('apps.core.urls')),
    path('alunos/', include('apps.alunos.urls')),
    path('rooms/', include('apps.rooms.urls')),
    path('school/', include('apps.school.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
