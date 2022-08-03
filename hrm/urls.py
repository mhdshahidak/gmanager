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

]