from django.urls import path
from app5 import views

urlpatterns = [
    path('ai_help', views.ai_help),
    path('chat_help', views.chat_help),
    path('faq', views.faq)
]