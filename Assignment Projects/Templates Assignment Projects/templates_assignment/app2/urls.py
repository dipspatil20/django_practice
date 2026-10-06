from django.urls import path
from app2 import views

urlpatterns = [
    path('electonics',views.Electronics),
    path('fashion',views.Fashion),
    path('groceries', views.Groceries)
]
