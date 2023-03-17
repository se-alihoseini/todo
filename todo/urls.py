from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('add/', views.AddTask.as_view(), name='add_task'),
    path('old/', views.OldTask.as_view(), name='old_task'),
    path('done/<int:task_id>', views.DoneTask.as_view(), name='done_task'),
    path('detail/<int:task_id>', views.DetailTask.as_view(), name='detail_task'),
]
