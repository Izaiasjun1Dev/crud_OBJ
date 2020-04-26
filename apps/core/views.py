from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.alunos.models import Aluno

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)
