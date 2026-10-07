from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_affairs, name='current_affairs'),
    path('disaster', views.disaster,name='disaster'),
    path('national',views.national, name='national'),
    path('political', views.political, name='political')
]
