from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('updation', views.updation, name='updation'),

]