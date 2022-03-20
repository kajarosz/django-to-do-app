from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('taskdelete/<int:pk>', views.taskdelete, name='taskdelete'),
    path('taskedit/<int:pk>', views.taskedit, name='taskedit'),
    path('taskcomplete/<int:pk>', views.taskcomplete, name='taskcomplete'),
    path('taskuncomplete/<int:pk>', views.taskuncomplete, name='taskuncomplete'),
]