from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('',views.employeeHome,name='employeehome'),

    path('allprojects',views.allProjects,name='allprojects'),
    path('projectsrs',views.projectSrs,name='projectsrs'),
    path('emprework',views.empRework,name='emprework'),
    path('dailyprogress',views.empDailyProgress,name='dailyprogress'),
    path('progressreport',views.empProgressReport,name='progressreport'),   
    path('emptask',views.empTask,name='emptask'),
    path('emphomework',views.empHomework,name='emphomework'),

    path('empattendance',views.empAttendance,name='empattendance'),

    path('allemployees',views.allEmployees,name='allemployees'),
    path('empdepartment',views.empDepartment,name='department'),
    path('emptimeline',views.empTimeline,name='emptimeline'),


    path('empteam',views.empTeam,name='empteam'),

    path('empprofile',views.empProfile,name='empprofile'),

]
