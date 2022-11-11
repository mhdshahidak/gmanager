from django.urls import path

from . import views

app_name = "ceo"

urlpatterns = [
    path("base", views.base, name="base"),
    # dashboard
    path("", views.log_in, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("ceodashboard", views.ceodashboard, name="ceodashboard"),
    path("crms", views.crm, name="crms"),
    path("employe", views.employe, name="employe"),
    # path('hr', views.hr, name='hr'),
    path("projectmanager", views.projectmanager, name="projectmanager"),
    # path('accounts', views.accounts, name='accounts'),
    # path('gm', views.gm, name='gm'),
    path("employeeprofile/<int:id>", views.employeeprofile, name="employeeprofile"),
    path("departmentwise", views.departmentwise, name="departmentwise"),
    path(
        "departmentwiseemployee/<int:id>",
        views.departmentwiseEmployee,
        name="departmentwiseemployee",
    ),
    path("employeelist", views.employeelist, name="employeelist"),
    path("allstaff", views.allstaff, name="allstaff"),
    path("dailychecked", views.dailychecked, name="dailychecked"),
    path("project", views.project, name="project"),
    path("projectlist/<str:selected_status>", views.projectlist, name="projectlist"),
    path("viewproject/<int:id>", views.viewproject, name="viewproject"),
    path("editemployee/<int:id>", views.editEmployeeDetails, name="editemployee"),
    path("rejectedlist", views.rejectedlist, name="rejectedlist"),
    path("viedetail/<int:id>", views.viedetails, name="viedetails"),
    path(
        "statusproject/<str:selected_status>", views.statusproject, name="statusproject"
    ),
    path(
        "statusviewproject/<int:id>", views.statusviewproject, name="statusviewproject"
    ),
    path("enquirylist", views.enquiryList, name="enquirylist"),

    path("listallproject", views.listallproject, name="listallproject"),
    path("clientlist", views.clientlist, name="clientlist"),

    ###############   pm features ##################

    path("enquiry-ceo", views.enquiryCeo, name="enquiryceo"),
    path("viewenquries-ceo/<str:id>", views.viewenquriesCeo, name="viewenquriesCeo"),
    path("proposal-ceo", views.proposalCeo, name="proposalCeo"),

    path("unassigneproject-ceo", views.unassigneprojectCeo, name="unassigneprojectCeo"),
    path("addproject-ceo/<str:id>", views.addprojectCeo, name="addprojectceo"),
    path("addteam-ceo/<str:id>", views.addteamCeo, name="addteamceo"),
    path("addschedule-ceo/<str:id>", views.addscheduleCeo, name="addscheduleCeo"),

    path("meetings-ceo", views.meetingsCeo, name="meetingsCeo"),
    path("srs-ceo", views.srsCeo, name="srsCeo"),


    

    # crm
    path("viewenquiry-ceo/<str:id>", views.viewenquiryCeo, name="viewenquiryCeo"),
    path("createproject-ceo/<str:id>", views.createProjectCeo, name="createprojectCeo"),

    # accounts
    path("accounts-praposal-ceo", views.praposalAccountsCeo, name="praposalAccountsCeo"),
    path("followuplist-ceo", views.followuplistceo, name="followuplistCeo"),

    #ajax
    # path("savaProposal", views.savaProposal, name="savaProposal"),



    
]
