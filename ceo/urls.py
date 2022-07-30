from django.urls import path
from . import views

app_name = 'ceo'

urlpatterns = [
    path('base', views.base, name='base'),
    # dashboard
    path('', views.admin, name='admin'),
    path('crm', views.crm, name='crm'),
    path('employee', views.employee, name='employee'),
    path('hr', views.hr, name='hr'),
    path('projectmanager', views.projectmanager, name='projectmanager'),
    path('accounts', views.accounts, name='accounts'),
    path('gm', views.gm, name='gm'),



    path('employeeprofile', views.employeeprofile, name='employeeprofile'),
]