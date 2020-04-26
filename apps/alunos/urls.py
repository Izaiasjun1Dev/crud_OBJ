from django.urls import path
from .views import AlunosList, AlunosEdit, AlunosDelete, AlunosCreate

urlpatterns = [
    path('', AlunosList.as_view(), name='alunos_list'),
    path('create/', AlunosCreate.as_view(), name='create_aluno'),
    path('editar/<int:pk>/', AlunosEdit.as_view(), name='alunos_edit'),
    path('delete/<int:pk>/', AlunosDelete.as_view(), name='alunos_delete')
]
