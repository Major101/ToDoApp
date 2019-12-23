from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add_to_do, name='add'),
    path('complete/<todo_id>', views.complete_to_do, name='complete'),
    path('delete-completed/', views.delete_completed, name='delete-completed'),
    path('delete-all/', views.delete_all, name='delete-all'),
]