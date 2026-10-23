from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_mov, name='create_mov'),
    path('read_mov', views.read_mov, name='read_mov'),
    path('update_mov/<int:mid>', views.update_mov, name='update_mov'),
    path('delete_mov/<int:mid>', views.delete_mov, name='delete_mov'),
]
