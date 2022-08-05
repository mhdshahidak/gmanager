from django.urls import path
from . import views

app_name = 'ceo'

urlpatterns = [
    path('base', views.base, name='base'),
    # dashboard
    path('', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('crm', views.crm, name='crm'),
    path('employee', views.employee, name='employee'),
    path('hr', views.hr, name='hr'),
    path('projectmanager', views.projectmanager, name='projectmanager'),
    path('accounts', views.accounts, name='accounts'),
    path('gm', views.gm, name='gm'),



    path('employeeprofile', views.employeeprofile, name='employeeprofile'),


    path('departmentwise', views.departmentwise, name='departmentwise'),
    path('employeelist', views.employeelist, name='employeelist'),
    path('allstaff', views.allstaff, name='allstaff'),
    path('dailychecked', views.dailychecked, name='dailychecked'),



    path('project', views.project, name='project'),
    path('projectlist', views.projectlist, name='projectlist'),
    path('viewproject', views.viewproject, name='viewproject'),

]