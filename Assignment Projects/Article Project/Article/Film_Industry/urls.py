from django.urls import path
from . import views

urlpatterns = [
    path('sandalwood', views.sandal, name='sandalwood'),
    path('mollywood', views.molly, name='mollywood'),
    path('bollywood',views.bolly, name='bollywood'),
    
]
