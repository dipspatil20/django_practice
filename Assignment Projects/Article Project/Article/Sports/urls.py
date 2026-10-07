from django.urls import path
from . import views

urlpatterns = [
    path('', views.sports, name='sports'),
    
    path('chess', views.chess,name='chess'),
    path('cricket',views.cricket, name='cricket'),
    path('hocky', views.hockey, name='hockey')
]
