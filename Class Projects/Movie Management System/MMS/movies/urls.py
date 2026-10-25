from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_mov, name='create_mov'),
    path('read_mov', views.read_mov, name='read_mov'),
    path('update_mov/<int:mid>', views.update_mov, name='update_mov'),
    path('delete_mov/<int:mid>', views.delete_mov, name='delete_mov'),

    # UsersModel
    path('create_users', views.create_users, name='create_u'),
    path('read_users', views.read_users, name='read_u'),
    path('update_users/<int:uid>', views.update_users, name='update_u'),
    path('delete_users/<int:uid>', views.delete_users, name='delete_u'),

    #BookingModel
    path('add_booking', views.add_booking, name='add_book'),
    path('read_booking', views.read_booking, name='read_book'),
    path('update_booking/<int:bid>', views.update_booking, name='update_book'),
    path('delete_booking/<int:bid>', views.delete_booking, name='delete_book'),
]
