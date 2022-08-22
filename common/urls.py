from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('base',views.base,name='base'),
    path('leaveapplication',views.leave_application,name='leaveapplication'),
    path('attendancereports',views.attendanceRreport,name='attendancereports'),
    path('settings',views.settings,name='settings'),
    path('leaves',views.leaves,name='leaves'),

    path('gohome',views.gohome,name='gohome'),
    path('excuse',views.excuse,name='excuse'),

]