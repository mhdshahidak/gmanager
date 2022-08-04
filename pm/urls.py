from django.urls import path
from . import views

app_name = 'pm'

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('viewenquries', views.viewenquries, name='viewenquries'),
    path('proposal', views.proposal, name='proposal'),

   

    path('project', views.project, name='project'),
    path('projectlist', views.projectlist, name='projectlist'),
    path('viewproject', views.viewproject, name='viewproject'),
    path('unassigneproject', views.unassigneproject, name='unassigneproject'),
    path('addschedule', views.addschedule, name='addschedule'),
    path('task', views.task, name='task'),
    path('viewtask', views.viewtask, name='viewtask'),
    path('srs', views.srs, name='srs'),


    path('dailyprogress', views.dailyprogress, name='dailyprogress'),
    path('viewdailyreport', views.viewdailyreport, name='viewdailyreport'),
    path('qcapprovel', views.qcapprovel, name='qcapprovel'),
    path('leaverequest', views.leaverequest, name='leaverequest'),

    
]