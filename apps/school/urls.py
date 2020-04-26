from django.urls import path
from .views import SchoolCreate, SchoolEdit

urlpatterns = [
    path('novo', SchoolCreate.as_view(), name='create_eschool'),
    path('editar/<int:pk>/', SchoolEdit.as_view(), name='edit_school'),
]
