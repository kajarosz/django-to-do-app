from django.urls import path
from . import views
from .views import ToDoListDeleteView

app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('taskdelete/<int:pk>', views.taskdelete, name='taskdelete'),
    path('taskedit/<int:pk>', views.taskedit, name='taskedit'),
    path('taskcomplete/<int:pk>', views.taskcomplete, name='taskcomplete'),
    path('taskuncomplete/<int:pk>', views.taskuncomplete, name='taskuncomplete'),
    path('todolistdelete/<int:pk>', ToDoListDeleteView.as_view(), name='todolistdelete'),
    path('todolistedit/<int:pk>', views.todolistedit, name='todolistedit'),
]