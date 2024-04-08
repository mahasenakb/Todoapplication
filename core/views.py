from django.shortcuts import render,redirect
from core.models import Todo

# Create your views here.
def home(request):
    if request.method=="POST":
        tododata=request.POST["todo"]
        res = Todo(todo=tododata)
        res.save()

    alltododata = Todo.objects.all()
    return render(request,"home.html", {'todos': alltododata})

def about(request):
    return render(request,"about.html")
    

def delete(request, pid):
    Todo.objects.get(uid = pid).delete()
    # Todo.objects.delete(uid = pid)
    return redirect("/")

def update(request, uid):
    if request.method=="POST":
        updatetodo=request.POST["mahasena"]
        res = Todo.objects.get(uid=uid)
        res.todo = updatetodo
        res.save()

    return redirect('/')
    




