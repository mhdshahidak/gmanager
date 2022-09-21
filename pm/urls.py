from django.urls import path
from . import views

app_name = 'pm'

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('viewenquries/<str:id>', views.viewenquries, name='viewenquries'),
    path('proposal', views.proposal, name='proposal'),

   

    path('project', views.project, name='project'),
    path('projectlist', views.projectlist, name='projectlist'),
    path('viewproject', views.viewproject, name='viewproject'),
    path('unassigneproject', views.unassigneproject, name='unassigneproject'),
    path('addproject/<str:id>', views.addproject, name='addproject'),
    path('addteam/<str:id>', views.addteam, name='addteam'),
    path('client', views.client, name='client'),
    path('addschedule/<str:id>', views.addschedule, name='addschedule'),
    path('task', views.task, name='task'),
    path('viewtask/<str:id>', views.viewtask, name='viewtask'),
    path('taskmember', views.taskmember, name='taskmember'),
    
    path('srs', views.srs, name='srs'),
    path('fullprojectlist', views.fullprojectlist, name='fullprojectlist'),


    path('dailyprogress', views.dailyprogress, name='dailyprogress'),
    path('viewdailyreport/<str:id>', views.viewdailyreport, name='viewdailyreport'),
    path('qcapprovel', views.qcapprovel, name='qcapprovel'),
    path('leaverequest', views.leaverequest, name='leaverequest'),

    path('meetings', views.meetings, name="meetings"),

    # ajax
    path('changeStatus', views.changeStatus, name='changeStatus'),
    path('savaProposal', views.savaProposal, name='savaProposal'),
    path('rejectedreason/<str:id>', views.rejectedreason, name='rejectedreason'),
    path('typereason', views.typereason, name='typereason'),
    path('leadersearch', views.leadersearch, name='leadersearch'),
    path('membersearch', views.membersearch, name='membersearch'),
    path('viedetails/<str:id>', views.viedetails, name='viedetails'),
    path('acceptdeatils/<str:id>', views.acceptdeatils, name='acceptdeatils'),
    path('rejectdeatils/<str:id>', views.rejectdeatils, name='rejectdeatils'),
    path('reason', views.reason, name='reason'),
    path('srsapprovel', views.srsapprovel, name='srsapprovel'),
    path('srsreject', views.srsreject, name='srsreject'),
    
    path('Changedailyreport/<str:id>', views.Changedailyreport, name='Changedailyreport'),
    path('changeqc', views.changeqc, name='changeqc'),
    path('rejectedqc/<str:id>', views.rejectedqc, name='rejectedqc'), 
    path('qcrework', views.qcrework, name='qcrework'),





    path('allstaff', views.allstaff, name='allstaff'),
    path('departmentwise', views.departmentwise, name='departmentwise'),
    path('employeelist/<int:id>',views.employeelist,name="employeelist"),
]    
