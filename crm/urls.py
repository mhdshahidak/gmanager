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
    # leave remove
    path("remove-leave/<int:id>", views.removeLeave, name="removeLeave"),

    # excuse
    path("excuse-crm", views.excuseCrm, name="excuseCrm"),
    path("excuse-report", views.excuseReport, name="excuseReport"),

    
    path("getemployeedata/<str:id>", views.getemployeedata, name="getemployeedata"),
    path("getemployeeleave/<str:id>", views.getemployeeleave, name="getemployeeleave"),
    path("adding-leave", views.leave, name="addingleave"),
    path("allstaff", views.allstaff, name="allstaff"),
    path("deleteemployee-crm/<str:id>", views.deleteemployeeCrm, name="deleteemployeeCrm"),
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

    # leave accepting
    path("acceptdeatils-crm/<str:id>", views.acceptdeatilsCrm, name="acceptdeatilscrm"),

    # pm features
    path("proposal-request-crm", views.proposalRequestCrm, name="proposalRequestCrm"),
    path("viewenquries-crm/<str:id>", views.viewenquriesCrm, name="viewenquriesCrm"),
    path("proposal-crm", views.proposalCrm, name="proposalCrm"),

    path("unassigneproject-crm", views.unassigneprojectCrm, name="unassigneprojectCrm"),
    path("addproject-crm/<str:id>", views.addprojectCrm, name="addprojectCrm"),
    path("addteam-crm/<str:id>", views.addteamCrm, name="addteamcrm"),
    path("addschedule-crm/<str:id>", views.addscheduleCrm, name="addscheduleCrm"),

    path("meetings-crm", views.meetingsCrm, name="meetingsCrm"),
    path("srs-crm", views.srsCrm, name="srsCrm"),
    path("qcapprovel-crm", views.qcapprovelCrm, name="qcapprovelCrm"),

    # Task
    path("crm-task", views.crmtask, name="crmtask"),
    path("crm-viewtask/<str:id>", views.crmviewtask, name="crmviewtask"),


    path("crm-taskteam/<int:id>", views.crmtaskteam, name="crmtaskteam"),

    # path("taskmember", views.taskmember, name="taskmember"),


    # ceo feature
    path(
        "statusproject-crm/<str:selected_status>", views.statusprojectCrm, name="statusprojectCrm"
    ),
    path(
        "statusviewproject-crm/<int:id>", views.statusviewprojectCrm, name="statusviewprojectCrm"
    ),


    # crm
    path("accounts-praposal-crm", views.praposalAccountsCrm, name="praposalAccountsCrm"),
    path("followuplist-crm", views.followuplistCrm, name="followuplistCrm"),





]
