from django.db import models
from apps.school.models import School
from django.urls import reverse
# Create your models here.

class Room(models.Model):
    Nome = models.CharField(max_length=100,
                            help_text='Nome da turma',
                            )
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse('list_turmas')
    
    def __str__(self):
        return self.Nome

    