from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_books, name='create_b'),
    path('read_books', views.read_books, name='read_b'),
    path('update_books/<int:bid>', views.update_books, name='update_b'),
    path('delete_books/<int:bid>', views.delete_books, name='delete_b'),

    path('create_users', views.create_users, name='create_u'),
    path('profile', views.profile, name='profile'),
    path('update_users/<int:uid>', views.update_users, name='update_u'),
    path('delete_users/<int:uid>',views.delete_users, name='delete_u'),
]
