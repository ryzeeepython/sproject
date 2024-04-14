
from django.urls import path, include
from .views import *

app_name = 'main'


urlpatterns = [
    path('', index, name = 'index'),
    path('register', registration, name = 'registration'),
    path('page_6', page_6, name = 'page_6'),
    path('auth', auth, name = 'auth'),
    path('lobby', lobby, name = 'lobby'),
    path('test', test, name = 'test'),
    path('page_1', page_1, name = 'page_1'),
    path('page_2', page_2, name = 'page_2'),
    path('page_3', page_3, name = 'page_3'),
    path('page_4', page_4, name = 'page_4'),
    path('page_5', page_5, name = 'page_5'), 
    path('logout', logout_user, name = 'logout'), 
    path('results', show_res, name = 'show_res'),
    path('download_file', download_file, name = 'download_file')
]
