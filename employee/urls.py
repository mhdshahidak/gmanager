from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('employeehome',views.employeeHome,name='employeehome'),

    path('allprojects',views.allProjects,name='allprojects'),
    path('emptask',views.empTask,name='emptask'),
    path('emphomework',views.empHomework,name='emphomework'),


    path('allemployees',views.allEmployees,name='allemployees'),
    path('empdepartment',views.empDepartment,name='department'),
    path('emptimeline',views.empTimeline,name='emptimeline'),


    path('empteam',views.empTeam,name='empteam'),

    path('empprofile',views.empProfile,name='empprofile'),

]
