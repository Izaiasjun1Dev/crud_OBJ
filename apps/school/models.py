from django.db import models
from django.urls import reverse

class School(models.Model):
    nome = models.CharField(max_length=100,
                            help_text='Nome da escola')
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('home')
    