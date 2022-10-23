from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('elem/', elem, name='elem'),
    path('selen/', selen, name='selen'),
    path('metallurg/', metallurg, name='metallurg'),
    path('rooms/', rooms, name='rooms'),
    path('service/', service, name='service'),
    path('stock/', stock, name='stock'),
    path('reviews/', reviews, name='reviews'),
]
