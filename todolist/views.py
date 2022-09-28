from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('user', user.id)
            response.set_cookie('username', username)
            return response
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def todolist(request):
    data = Task.objects.filter(user = request.COOKIES['user'])
    
    context = { 
        'item_list' : data,
        'last_login' : request.COOKIES['last_login'],
        'user' : request.COOKIES['username']
    }
    return render(request, 'todolist.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        user_id = request.COOKIES['user']
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        Task.objects.create(user = User.objects.get(pk = user_id), date = date, title = title, description = description)
        
        response = HttpResponseRedirect(reverse("todolist:todolist"))
        return response
    context = {}
    return render(request, 'create_task.html', context)