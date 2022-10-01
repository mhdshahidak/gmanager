from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("base", views.base, name="base"),
    path("", views.employeeHome, name="employeehome"),
    path("meetings/<int:id>", views.empMeetingLink, name="meetings"),
    path("allprojects", views.allProjects, name="allprojects"),
    # path('projectsrs',views.projectSrs,name='projectsrs'),
    path("emprework", views.empRework, name="emprework"),
    path("dailyprogress/<int:id>", views.empDailyProgress, name="dailyprogress"),
    path("progressreport/<int:id>", views.empProgressReport, name="progressreport"),
    path("emptask", views.empTask, name="emptask"),
    path("taskdetails/<int:id>", views.taskdetails, name="taskdetails"),
    path("taskreport/<int:id>", views.taskreport, name="taskreport"),
    path("emphomework", views.empHomework, name="emphomework"),
    path("leaveapplication", views.leaveApplication, name="leaveapplication"),
    path("empattendance", views.empAttendance, name="empattendance"),
    path("allemployees", views.allEmployees, name="allemployees"),
    path("empdepartment", views.empDepartment, name="department"),
    path(
        "departmentemployee/<int:id>",
        views.departmentwiseEmployee,
        name="departmentemployee",
    ),
    path("emptimeline", views.empTimeline, name="emptimeline"),
    path("empteam", views.empTeam, name="empteam"),
    path("empprofile", views.empProfile, name="empprofile"),
    path("viewproject", views.viewproject, name="viewproject"),
    path("getprofiledata/<int:id>", views.getprofiledata, name="getprofiledata"),
    path("getdata/<int:id>", views.getdata, name="getdata"),
    path("Reworkstatus", views.Reworkstatus, name="Reworkstatus"),
    path("projeclist", views.projeclist, name="projeclist"),
    path("detailview/<int:id>", views.detailview, name="detailview"),
    #    path('logout_view',views.logout_view,name='logout_view'),
    path("countval", views.countval, name="countval"),
]
