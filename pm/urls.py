from django.urls import path
from . import views

app_name = 'pm'

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('viewenquries', views.viewenquries, name='viewenquries'),
]