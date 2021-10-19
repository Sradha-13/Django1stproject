from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

def todo_list(request):
    Todos=Todo.objects.all()
    #print(Todos)
    context={
       "todo_list": Todos
   }
    return render(request,"todo_list.html",context)

#CURD- Creat,Update,Delete,List,Rtrive/Read

def todo_details(request,id):
   todo= Todo.objects.get(id=id)
   context={
      "Todo": todo
   }
   return render(request,"todo_details.html",context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form" : form}
    return render(request, "todo_create.html", context)

def todo_update(request,id):
    todo= Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form" : form}
    return render(request, "todo_update.html", context)
def todo_delete(request,id):
   todo= Todo.objects.get(id=id)
   todo.delete()
   return redirect('/')

