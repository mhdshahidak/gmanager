from django.urls import path
from . import views

app_name = 'hrm'

urlpatterns = [
    path('', views.hrmHome, name="hrhome"),
    path('employees', views.employeeList, name="employees"),
    path('clientlist', views.clientList, name="clientlist"),
    path('leaverequest', views.leaveRequest, name="leaverequest"),
    path('leavereport', views.leaveReport, name="leavereport"),
    path('attantancereport', views.attantanceReport, name="attantancereport"),
    path('hrsettings', views.hrsettings, name="hrsettings"),
    path('attantancelist', views.attantanceList, name="attantancelist"),
    path('hrmaccept/<str:id>', views.hrmaccept, name="hrmaccept"),
    path('excuse', views.excuse, name="excuse"),
    path('changevalue', views.changevalue, name="changevalue"),
    path('team', views.team, name="team"),
    path('addteam/<str:id>', views.addteam, name="addteam"),



    path('getemployeedata/<str:id>', views.getemployeedata, name="getemployeedata"),
    path('getemployeeleave/<str:id>', views.getemployeeleave, name="getemployeeleave"),
    path('leave', views.leave, name="leave"),
    
    path('addingattendence', views.addingattendence, name="addingattendence"),


    


    
]