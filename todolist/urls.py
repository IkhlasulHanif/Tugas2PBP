from django.urls import path
from todolist.views import create_task, logout_user, register 
from todolist.views import todolist
from todolist.views import login_user 

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]
