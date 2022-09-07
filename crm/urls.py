from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.crmHome, name="crmhome"),
    path('enquirylist', views.enquiryList, name="enquirylist"),
    path('clientlist', views.clientList, name="clientlist"),
    path('projectlist', views.projectList, name="projectlist"),
    path('followuplist', views.followUpList, name="followuplist"),
    path('feedback', views.feedBack, name="feedback"),
    path('leaves', views.leaves, name="leaves"),
    path('attantance', views.attantance, name="attantance"),
    path('settings', views.settings, name="settings"),
    path('profile', views.profile, name="profile"),
    path('viewenquiry/<str:id>', views.viewenquiry, name="viewenquiry"),

    path('createproject/<str:id>',views.createProject,name='createproject'),
    path('viewdata/<str:id>',views.viewdata,name='viewdata'),
    path('changedata/<str:id>',views.changedata,name='changedata'),
    
    


    path('attantancelist', views.attantanceList, name="attantancelist"),
    path('attantancereport', views.attantanceReport, name="attantancereport"),
    path('getemployeedata/<str:id>', views.getemployeedata, name="getemployeedata"),
    path('getemployeeleave/<str:id>', views.getemployeeleave, name="getemployeeleave"),



    path('allstaff', views.allstaff, name='allstaff'),
    path('departmentwise', views.departmentwise, name='departmentwise'),
    path('employeelist/<int:id>',views.employeelist,name="employeelist"),
    path('addclient', views.addclient, name='addclient'),



    
]   