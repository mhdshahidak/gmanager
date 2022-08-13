from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('leaveapplication',views.leave_application,name='leaveapplication'),
    path('attendancereports',views.attendanceRreport,name='attendancereports'),
    path('settings',views.settings,name='settings'),

]