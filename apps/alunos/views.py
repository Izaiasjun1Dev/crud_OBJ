from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class AlunosList(ListView):
    model = Aluno

    def get_queryset(self):
        school_logada = self.request.user.aluno.school
        return Aluno.objects.filter(school=school_logada)
    
class AlunosEdit(UpdateView):
        model = Aluno
        fields = ['nome', 'email', 'room' ]
        
class AlunosDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('alunos_list')
    
class AlunosCreate(CreateView):
    model = Aluno
    fields = ['nome', 'email', 'room']
        
    def form_valid(self, form):
        aluno_obj = form.save(commit=False)
        username = aluno_obj.nome.split(' ')[0] + aluno_obj.nome.split(' ')[1]
        aluno_obj.school = self.request.user.aluno.school
        aluno_obj.user = User.objects.create(
            username=username
        )
        aluno_obj.save()
        return super(aluno_obj, self).form_valid(form)
        
        
        
    