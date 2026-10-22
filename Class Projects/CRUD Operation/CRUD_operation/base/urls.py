from django.urls import path
from . import views

urlpatterns = [
    path('',views.create, name='create'),
    path('read', views.read, name='read'),
    path('update/<int:eid>/', views.update, name='update'),
    path('delete/<int:eid>/', views.delete, name='delete')
]
