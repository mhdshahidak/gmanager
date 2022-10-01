from django.urls import path

from . import views

app_name = "gm"

urlpatterns = [
    path("base", views.base, name="base"),
    path("", views.home, name="home"),
    path("paymentdetails", views.paymentdetails, name="paymentdetails"),
    path("viewhistory", views.viewhistory, name="viewhistory"),
    path("salary", views.salary, name="salary"),
    path("projectlist", views.projectlist, name="projectlist"),
]
