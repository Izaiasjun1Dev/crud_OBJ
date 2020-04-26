from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import School

class SchoolCreate(CreateView):
    model = School
    fields = ['nome']
    
    def form_validate(self, form):
        obj =  form.save()
        aluno = self.request.user.aluno
        aluno.school = obj
        aluno.save()
        
class SchoolEdit(UpdateView):
    model = School
    fields = ['nome']