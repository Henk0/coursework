from django.urls import path
from .views import *

urlpatterns = [
    path('', station_list, name='station_list'),
    path('schedule/<station>', station, name='station'),
    path('train/<t_id>', train, name='train'),
    path('login', login, name='login'),
    path('auth', auth, name='auth'),
    path('add_train', add_train, name='add_train'),
    path('add_station', add_station, name='add_station'),
    path('edit_train', edit_train, name='edit_train')
]
