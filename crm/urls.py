from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('',views.crmHome,name="crmhome"),
    path('enquirylist',views.enquiryList,name="enquirylist"),
]