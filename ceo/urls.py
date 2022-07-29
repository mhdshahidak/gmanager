from django.urls import path
from . import views

app_name = 'ceo'

urlpatterns = [
    path('base', views.base, name='base')
]