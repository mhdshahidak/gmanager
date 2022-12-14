from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("base", views.base, name="base"),
    path("", views.home, name="home"),
    path("praposal", views.praposal, name="praposal"),
    path("followuplist", views.followuplist, name="followuplist"),
    path("completed", views.completed, name="completed"),
    path("updation", views.updation, name="updation"),
    path("changebill", views.changebill, name="changebill"),
    path("changefollow", views.changefollow, name="changefollow"),
    path("viedetails/<str:id>", views.viedetails, name="viedetails"),
]
