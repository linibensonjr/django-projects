from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasklist'),
    path('update_task/<str:pk>/', views.updateTask, name='update')
]
