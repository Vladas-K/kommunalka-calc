from django.urls import path
from .views import calculate, history

urlpatterns = [
    path('', calculate, name='calculate'),
    path('history/', history, name='history'),
]
