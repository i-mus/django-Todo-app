from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from todoapp.forms import Todoform
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Taskkdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk': self.object.id})


class taskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'


# Create your views here.
def index(request):
    taskAll = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        newtask = Task(name=name, priority=priority, date=date)
        newtask.save()
    return render(request, 'index.html', {'task': taskAll})


def delete(request, id):
    taskdone = Task.objects.get(id=id)
    if request.method == 'POST':
        taskdone.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
