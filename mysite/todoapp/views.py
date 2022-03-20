from audioop import reverse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import TaskForm, ToDoListForm
from .models import Task, ToDoList
from django.views.generic import DeleteView

# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.POST.get('add-task'):
            form = TaskForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, ('Task has been added to the list!'))
                return redirect(reverse('todoapp:home'))
        elif request.POST.get('add-list'):
            form = ToDoListForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, ('New task list created successfuly!'))
                return redirect(reverse('todoapp:home'))
    else:
        todolists = ToDoList.objects.all()
        completed_tasks = Task.objects.filter(completed=True)
        uncompleted_tasks = Task.objects.filter(completed=False)
        return render(request, 'todoapp/home.html', {'completed_tasks': completed_tasks, 'uncompleted_tasks': uncompleted_tasks, 'todolists': todolists})

def taskdelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    messages.success(request, ('Task has been deleted'))
    return redirect(reverse('todoapp:home'))

def taskedit(request, pk):
    if request.method == 'POST':
        if request.POST.get('save'):
            task = Task.objects.get(pk=pk)
            form = TaskForm(request.POST or None, instance=task)
            if form.is_valid():
                form.save()
                messages.success(request, ('Task has been edited!'))
                return redirect(reverse('todoapp:home'))
        elif request.POST.get('cancel'):
            return redirect(reverse('todoapp:home'))
    else:
        task = Task.objects.get(pk=pk)
        return render(request, 'todoapp/taskedit.html', {'task': task})

def taskcomplete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect(reverse('todoapp:home'))
    

def taskuncomplete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = False
    task.save()
    return redirect(reverse('todoapp:home'))

class ToDoListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('todoapp:home')
 