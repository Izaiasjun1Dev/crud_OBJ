from django.shortcuts import render
from .models import Room
from django.views.generic import (DeleteView, 
                                  ListView, 
                                  CreateView, 
                                  UpdateView)
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

class RoomsList(ListView):
    model = Room
    
    def get_queryset(self):
        school_log = self.request.user.aluno.school
        return Room.objects.filter(school=school_log)
    
class RoomsCreate(CreateView):
    model = Room
    fields = ['Nome']
    
    def form_valid(self, form):
        room = form.save(commit=False)
        room.school = self.request.user.aluno.school
        room.save()
        return super(RoomsCreate, self).form_valid(form)
    
class RoomsEdit(UpdateView):
    model = Room
    fields = ['Nome']
    
class RoomsDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('list_turmas')
        
        