from django.urls import path
from . import views

urlpatterns=[
    path('',views.create,name='create'),
    path('read',views.read,name='read'),
    path('update/<int:tid>',views.update,name='update'),
    path('delete/<int:tid>',views.delete,name='delete'),

    path('create_cat',views.create_cat,name='create_cat'),
    path('read_cat',views.read_cat,name='read_cat'),
    path('update_cat/<int:tid>',views.update_cat,name='update_cat'),
    path('delete_cat/<int:tid>',views.delete_cat,name='delete_cat'),

    path('create_rec',views.create_rec,name='create_rec'),
    path('read_rec',views.read_rec,name='read_rec'),
    path('update_rec/<int:tid>',views.update_rec,name='update_rec'),
    path('delete_rec/<int:tid>',views.delete_rec,name='delete_rec'),
]
