from django.urls import path
from app4 import views

urlpatterns = [
    path('create_profile', views.create_profile),
    path('display_profile', views.display_profile),
    path('update_profile', views.update_profile)
]
