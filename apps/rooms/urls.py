from django.urls import path
from .views import (RoomsList, 
                    RoomsCreate, 
                    RoomsEdit, 
                    RoomsDelete)

urlpatterns = [
    path('list', RoomsList.as_view(), name='list_turmas'),
    path('create', RoomsCreate.as_view(), name='create_turma'),
    path('editar/<int:pk>', RoomsEdit.as_view(), name='edit_turmas'),
    path('delete/<int:pk>', RoomsDelete.as_view(), name='delete_turmas'),

]