from django.urls import path

from . import views

app_name = "crm"

urlpatterns = [
    path("", views.crmHome, name="crmhome"),
    path("enquirylist", views.enquiryList, name="enquirylist"),
    path("graphicenquiry", views.graphicenquiry, name="graphicenquiry"),
    path(
        "viewgraphicenquries/<str:id>",
        views.viewgraphicenquries,
        name="viewgraphicenquries",
    ),
    path("clientlist", views.clientList, name="clientlist"),
    path("projectlist", views.projectList, name="projectlist"),
    path("followuplist", views.followUpList, name="followuplist"),
    path("feedback", views.feedBack, name="feedback"),
    path("leaves", views.leaves, name="leaves"),
    path("attantance", views.attantance, name="attantance"),
    path("settings", views.settings, name="settings"),
    path("profile", views.profile, name="profile"),
    path("viewenquiry/<str:id>", views.viewenquiry, name="viewenquiry"),
    path("createproject/<str:id>", views.createProject, name="createproject"),
    path("viewdata/<str:id>", views.viewdata, name="viewdata"),
    path("changedata/<str:id>", views.changedata, name="changedata"),
    path("proposal", views.proposal, name="proposal"),
    path("savaProposal", views.savaProposal, name="savaProposal"),
    path("rejectedreason/<str:id>", views.rejectedreason, name="rejectedreason"),
    path("typereason", views.typereason, name="typereason"),
    path("attantancelist", views.attantanceList, name="attantancelist"),
    path("attantancereport", views.attantanceReport, name="attantancereport"),
    path("getemployeedata/<str:id>", views.getemployeedata, name="getemployeedata"),
    path("getemployeeleave/<str:id>", views.getemployeeleave, name="getemployeeleave"),
    path("adding-leave", views.leave, name="addingleave"),
    path("allstaff", views.allstaff, name="allstaff"),
    path("departmentwise", views.departmentwise, name="departmentwise"),
    path("employeelist/<int:id>", views.employeelist, name="employeelist"),
    path("addclient", views.addclient, name="addclient"),
    path("deleteenquery/<int:id>", views.deleteenquery, name="deleteenquery"),
    path("editclient/<int:id>", views.editclient, name="editclient"),
    path("deleteclient/<int:id>", views.deleteclient, name="deleteclient"),
    path("unassigneproject", views.unassigneproject, name="unassigneproject"),
    path("addproject/<str:id>", views.addproject, name="addproject"),
    path("addteam/<str:id>", views.addteam, name="addteam"),
    path("addschedule/<str:id>", views.addschedule, name="addschedule"),
    path("meetinglist", views.meetinglist, name="meetinglist"),
    path("meetingapproved", views.meetingapproved, name="meetingapproved"),
    path("dailyprogress", views.dailyprogress, name="dailyprogress"),
    path("leaverequest", views.leaverequest, name="leaverequest"),
    path("leavereport", views.leavereport, name="leavereport"),
    
    path("leavestatus", views.leavestatus, name="leavestatus"),
    path("viewdailyreport/<str:id>", views.viewdailyreport, name="viewdailyreport"),
    path(
        "Changedailyreport/<str:id>", views.Changedailyreport, name="Changedailyreport"
    ),
]
