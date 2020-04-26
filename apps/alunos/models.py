from django.db import models
from django.contrib.auth.models import User
from apps.rooms.models import Room
from apps.school.models import School
from django.urls import reverse


class Aluno(models.Model):
    nome = models.CharField(max_length=100,
                            blank=True, null=True)
     
    email = models.CharField(max_length=50)
    
    user = models.OneToOneField(User, 
                             on_delete=models.PROTECT)
    
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    
    school = models.ForeignKey(School, 
                              on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('alunos_list')
    
    def __str__(self):
        return self.nome
    
