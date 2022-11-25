from django.http import HttpResponse
from django.shortcuts import render

from todoapp.models import Task


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        newtask = Task(name=name, priority=priority)
        newtask.save()
    return render(request, 'index.html')
