from django.shortcuts import render
from .models import Ishchilar

def home(request):
    return render(request, 'index.html')
