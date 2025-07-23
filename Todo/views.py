from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    datos = Todo.objects.all()
    context = {
        'todo':datos
    }
    return render(request, 'todo/index.html',context)

#mostrar datos de una tarea
@login_required
def view(request, id):
    hw = Todo.objects.get(id=id)
    return render(request, 'todo/detail.html',{'hw':hw})

#crear una nueva tarea 
@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()
        context = {
            'form':form
        }
        return render(request, 'todo/create.html', context)
#edicion de una tarea 
@login_required
def edit(request, id):
    hw = Todo.objects.get(id=id)
    if request.method == "GET":
        form = TodoForm(instance=hw)
        context = {
            'form': form,
            'id':id
        }
        return render(request, 'todo/edit.html', context)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=hw)
        if form.is_valid():
            form.save()
        return redirect('todo')

@login_required
def delete(request, id):
    hw = Todo.objects.get(id=id)
    hw.delete()
    return redirect('todo')
