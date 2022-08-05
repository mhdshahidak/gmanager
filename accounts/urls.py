from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.home, name='home'),
    path('praposal', views.praposal, name='praposal'),

    path('followuplist', views.followuplist, name='followuplist'),
    path('completed', views.completed, name='completed'),
    path('updation', views.updation, name='updation'),
    
    ]