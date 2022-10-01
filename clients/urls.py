from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("base", views.base, name="base"),
    # path('', views.home, name='home'),
    path("", views.home, name="home"),
    path("viewproject/<str:id>", views.viewproject, name="viewproject"),
    path("updation", views.updation, name="updation"),
    path("payment", views.payment, name="payment"),
    path("completedproject", views.completedproject, name="completedproject"),
    path("Getid/<str:id>", views.Getid, name="Getid"),
    path("clientrework", views.clientrework, name="clientrework"),
]
