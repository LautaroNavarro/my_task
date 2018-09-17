from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from apps.todo_list.models import Priority, Estate, Task
from apps.todo_list.forms import TaskForm

# Create your views here.


def ShowTaskFunction(request):
    options = Priority.objects.all()
    if request.GET.get("priority", "") != "":
        parameter = request.GET.get("priority", "")
        tasks = Task.objects.filter(priority__name=parameter).order_by('id')
    elif request.GET.get("estate", "") != "":
        parameter = request.GET.get("estate", "")
        tasks = Task.objects.filter(estate__name=parameter).order_by('id')
    else:
        tasks = Task.objects.order_by('create_date').order_by('id')
    return render(request, 'task/show_task.html', {'object_list': tasks, 'options': options})


class CreateTask (CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create_task.html'
    success_url = 'http://127.0.0.1:8000/show_tasks/'


def do_task(request):
    options = Priority.objects.all()
    if request.GET.get("id_task", "") != "":
        id_task = request.GET.get("id_task", "")
        done = Estate.objects.get(name='Done')
        task = Task.objects.filter(id=id_task)
        task.update(estate=done)
        return redirect("http://127.0.0.1:8000/show_tasks/")
    else:
        return redirect("http://127.0.0.1:8000/show_tasks/")
