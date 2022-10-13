from django.urls import path
from todolist.views import create_task, logout_user, register, delete_task, is_finished, is_not_finished, show_json, add_todolist_item
from todolist.views import todolist
from todolist.views import login_user 

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('<int:id>', delete_task, name = 'delete_task'),
    path('<int:id>/finished', is_finished, name ='finished'),
    path('<int:id>/not-finished', is_not_finished, name='not_finished'),
    path('json/', show_json, name='show_json'),
    path('add/', add_todolist_item, name="add_todolist_item")
    
]
