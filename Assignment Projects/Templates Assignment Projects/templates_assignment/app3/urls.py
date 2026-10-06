from django.urls import path
from app3 import views

urlpatterns = [
    path('items', views.Items),
    path('add_item', views.Add_item),
    path('remove_item', views.Remove_item)
]
