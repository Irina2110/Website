from .forms import TaskForm,NotesForm
from django.shortcuts import render,redirect
from . models import Task,Notes
from . forms import Task,Notes

def index (request):
    tasks= Task.objects.order_by('id')
    return render(request,'main/index.html',{'title':'Главная страница сайта',"tasks":tasks})

def about(request):
    return render(request,'main/about.html')

def create (request):
    error=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма была неверной'
    form=TaskForm()
    context={
        'form': form,
        'error': error
    }
    return render(request,'main/create.html',context)

def post_home (request):
    posts= Notes.objects.all()
    return render(request,'main/post.html',{"posts":posts})

def create_post(request):
    error=''
    if request.method=='POST':
        form=NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error= 'Форма была неверной'

    form =NotesForm()
    data= {
        'form': form,
        'error':error
    }
    return render(request,'main/create_post.html')

