from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from crm.form import ClientForm, EnquiryForm
from pm.form import PraposalpdfForm, ProjectForm


from crm.models import EnquiryNote
from pm.models import (
    SRS,
    DailyProgress,
    Enquiry,
    Meeting,
    Praposalpdf,
    Project,
    ProjectMembers,
    ProjectProgressFiles,
    ProjectStatus,
)

# from django.contrib.auth import login as auth_login
# Create your views here.
from ceo.form import RegisterForm
from .models import Client, EmergenctContact, Employees, SubCatagory


def base(request):
    return render(request, "ceo/partials/base.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect("ceo:ceodashboard")
            elif user.client != None:
                return redirect("clients:home")
            elif user.employee.catagory.catagory.catagory_title == "HRM":
                return redirect("hrm:hrhome")
            elif user.employee.catagory.catagory.catagory_title == "CRM":
                return redirect("crm:crmhome")
            elif user.employee.catagory.catagory.catagory_title == "PM":
                return redirect("pm:index")
            elif user.employee.catagory.catagory.catagory_title == "GM":
                return redirect("gm:home")
            elif user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
                return redirect("accounts:home")
            elif user.employee.catagory.catagory.catagory_title == "EMPLOYEE":
                return redirect("employee:employeehome")

        else:

            context = {
                "status": 1,
            }
            return render(request, "ceo/login.html", context)

    return render(request, "ceo/login.html")


def logout_view(request):
    logout(request)
    return redirect("ceo:login")


@login_required(login_url="/")
def ceodashboard(request):
    # projects = ProjectStatus.objects.filter(status="Not Started",).count()
    clients = Client.objects.all().count()
    employees = Employees.objects.all().count()

    # enquirylist = EnquiryNote.objects.filter(status = 'Active').count()
    # addedtoprop = Enquiry.objects.filter(status = 'Added To Proposal').count()
    # billcreation = Enquiry.objects.filter(status = 'Bill Creation').count()
    # billadvance = Enquiry.objects.filter(status = 'Bill Advance').count()
    # advancepaid = Enquiry.objects.filter(status = 'Advance Paid').count()
    # enquirylist = EnquiryNote.objects.filter(status = 'Active').count()
    enquirylist = Enquiry.objects.filter(status="Enquiry").count()
    enquirylist1 = EnquiryNote.objects.filter(status="Active").count()

    addedtoprop = Enquiry.objects.filter(status="Added To Proposal").count()
    billcreation = Enquiry.objects.filter(status="Bill Creation").count()
    billadvance = Enquiry.objects.filter(status="Bill Advance").count()
    advancepaid = Enquiry.objects.filter(status="Advance Paid").count()
    rejected = Enquiry.objects.filter(status="Rejected").count()
    notstated = ProjectStatus.objects.filter(status="Not Started").count()
    ongoing = ProjectStatus.objects.filter(status="On Going").count()
    onscheduling = ProjectStatus.objects.filter(status="On Scheduling").count()
    delayed = ProjectStatus.objects.filter(status="Delayed").count()
    qc = ProjectStatus.objects.filter(status="Qc").count()
    w4c = ProjectStatus.objects.filter(status="W4C").count()
    rework = ProjectStatus.objects.filter(status="Rework").count()
    completed = ProjectStatus.objects.filter(status="Completed").count()
    projects=notstated+ongoing+onscheduling+delayed+qc+w4c+rework+completed

    print(billcreation,"#"*10)

    context = {
        "is_ceodashboard": True,
        "projects": projects,
        "clients": clients,
        "employees": employees,
        "addedtoprop": addedtoprop,
        "billcreation": billcreation,
        "billadvance": billadvance,
        "advancepaid": advancepaid,
        "rejected": rejected,
        "enquirylist": enquirylist,
        "notstated": notstated,
        "ongoing": ongoing,
        "delayed": delayed,
        "onscheduling": onscheduling,
        "qc": qc,
        "w4c": w4c,
        "rework": rework,
        "completed": completed,
        "enquirylist1":enquirylist1
    }
    return render(request, "ceo/dashboard/admin.html", context)


@login_required(login_url="/")
def crm(request):

    if request.method == "POST":

        instructions = request.POST["instruction"]

        new_project_note = EnquiryNote(description=instructions)
        new_project_note.save()
        context = {
            "is_crm": True,
        }
    else:

        context = {
            "is_crms": True,
        }
        return render(request, "ceo/dashboard/crm.html", context)
    return render(request, "ceo/dashboard/crm.html", context)


@login_required(login_url="/")
def employe(request):
    # empllist = Employees.objects.filter(catagory__catagory__catagory_title='EMPLOYEE')
    empllist = Employees.objects.all()
    emp_count = Employees.objects.all().count()

    context = {
        "is_employe": True,
        "empllist": empllist,
        "emp_count": emp_count,
    }
    return render(request, "ceo/dashboard/employee.html", context)


# def hr(request):
#     return render (request,'ceo/dashboard/hr.html')


@login_required(login_url="/")
def projectmanager(request):
    context = {
        "is_projectmanager": True,
    }
    return render(request, "ceo/dashboard/projectmanager.html", context)


# def accounts(request):
#     return render (request,'ceo/dashboard/accounts.html')


# def gm(request):
#     return render (request,'ceo/dashboard/gm.html')


def employeeprofile(request, id):
    employedetails = Employees.objects.get(id=id)
    primarycontact = EmergenctContact.objects.get(employee=employedetails)

    # employeedata=Employees.objects.get(id=request.user.employee.id)
    team = ProjectStatus.objects.filter(
        member__team=employedetails
    ) 
    lead= ProjectStatus.objects.filter(member__lead=employedetails)
    # procount = ProjectStatus.objects.filter(member__team=employedetails,status='On Going') |ProjectStatus.objects.filter(member__lead=employedetails,status='On Going').count()

    context = {
        "employedetails": employedetails,
        "primarycontact": primarycontact,
        "team": team,
        "lead":lead

    }
    return render(request, "ceo/employeeprofile.html", context)


@login_required(login_url="/")
def departmentwise(request):
    department = SubCatagory.objects.all()

    class cat:
        def __init__(self, title, counts, id):
            self.title = title
            self.counts = counts
            self.id = id

    estimatelist = []
    for i in department:
        id = i.id
        emp_count = Employees.objects.filter(catagory=i).count()

        estimatelist.append(cat(i, emp_count, id))

    context = {
        "is_departmentwise": True,
        "emp_count": estimatelist,
        # "departments":department,
    }
    return render(request, "ceo/departmentwise.html", context)


@login_required(login_url="/")
def departmentwiseEmployee(request, id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {"category": category, "employees": employees}
    return render(request, "ceo/departmentwise_employee.html", context)


@login_required(login_url="/")
def employeelist(request):
    return render(request, "ceo/employeelist.html")


@login_required(login_url="/")
def allstaff(request):
    all_emp = Employees.objects.all().order_by("name")
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            form_data = Employees.objects.get(id=data.id)

            User = get_user_model()
            User.objects.create_user(
                username=form_data.username,
                password=form_data.password,
                employee=form_data,
            )
            emergecy = EmergenctContact(employee=form_data)
            emergecy.save()

            return redirect("ceo:allstaff")
        else:
            pass

    else:
        context = {
            "is_allstaff": True,
            "form": RegisterForm,
            "employees": all_emp,
        }
        return render(request, "ceo/allstaff.html", context)
    context = {
        "is_allstaff": True,
        # "employees":all_emp,
    }
    return render(request, "ceo/allstaff.html", context)


@login_required(login_url="/")
def editEmployeeDetails(request, id):
    n = Employees.objects.get(id=id)
    if request.method == "POST":
        form = RegisterForm(request.POST or None, instance=n)
        if form.is_valid():
            data = form.save()
            password_upadte = get_user_model().objects.get(employee=n)
            password_upadte.set_password(data.password)
            password_upadte.save()
            get_user_model().objects.filter(employee=n).update(username=data.username)
            return redirect("ceo:allstaff")
    else:
        form = RegisterForm(request.POST or None, instance=n)
    context = {
        "form": form,
    }
    return render(request, "ceo/edit_employee.html", context)


@login_required(login_url="/")
def dailychecked(request):
    if request.method == "POST":
        serachdate = request.POST["serachdate"]
        print(serachdate)
        if DailyProgress.objects.filter(date=serachdate).exists():
            print("exist")
            projectlists = DailyProgress.objects.filter(date=serachdate)
            context = {
                "is_dailychecked": True,
                "projectlists": projectlists,
                "status": 0,
            }
            return render(request, "ceo/dailychecked.html", context)
        else:
            print("not exist")
            context = {"is_dailychecked": True, "status": 1}
            return render(request, "ceo/dailychecked.html", context)
    else:

        context = {
            "is_dailychecked": True,
        }
        return render(request, "ceo/dailychecked.html", context)


@login_required(login_url="/")
def project(request):
    context = {
        "is_project": True,
    }
    return render(request, "ceo/project/project.html", context)


@login_required(login_url="/")
def rejectedlist(request):
    rejected = Enquiry.objects.filter(status="Rejected")
    context = {"is_project": True, "rejected": rejected}
    return render(request, "ceo/rejectedlist.html", context)


@login_required(login_url="/")
def projectlist(request, selected_status):
    projects = Enquiry.objects.filter(status=selected_status)
    context = {
        "is_project": True,
        "projects": projects,
    }
    return render(request, "ceo/project/projectlist.html", context)


@login_required(login_url="/")
def viewproject(request, id):
    enquiry = Enquiry.objects.get(id=id)
    if Praposalpdf.objects.filter(enquiry=enquiry).exists:
        propsosal = Praposalpdf.objects.filter(enquiry=enquiry)
        print(propsosal, "#" * 10)
        context = {"is_project": True, "enquiry": enquiry, "propsosal": propsosal}
        return render(request, "ceo/project/viewproject.html", context)
    else:
        context = {"is_project": True, "enquiry": enquiry}
        return render(request, "ceo/project/viewproject.html", context)


@csrf_exempt
def viedetails(request, id):
    getdata = Enquiry.objects.get(id=id)
    data = {
        "reason": getdata.reason,
    }

    return JsonResponse({"value": data})


def handler404(request, exception):
    return render(request, "error/404.html", status=404)


def handler500(request, *args, **argv):
    response = render("error/500.html")
    response.status_code = 500
    return response


def statusproject(request, selected_status):
    allproject = ProjectStatus.objects.filter(status=selected_status)
    context = {
        "allproject": allproject,
    }
    return render(request, "ceo/statusproject.html", context)


def statusviewproject(request, id):

    projectdetail = Project.objects.get(id=id)
    daily_report = DailyProgress.objects.filter(project=projectdetail).values(
        "date", "status", "note", "employee__name"
    )
    progressreport = ProjectStatus.objects.get(project=projectdetail)
    members = ProjectMembers.objects.filter(project=projectdetail)
    viewsrs = SRS.objects.get(project=projectdetail)
    uploadedfiles = ProjectProgressFiles.objects.filter(project=projectdetail).exclude(
        files="New default that isn't None"
    )
    context = {
        "projectdetail": projectdetail,
        "daily_report": daily_report,
        "progressreport": progressreport,
        "members": members,
        "viewsrs": viewsrs,
        "uploadedfiles": uploadedfiles,
    }
    return render(request, "ceo/statusviewproject.html", context)



@login_required(login_url="/")

def enquiryList(request):
    enquirylistdata = EnquiryNote.objects.filter(status="Active")
    context = {"is_enquiryList": True, "enquirylistdata": enquirylistdata}
    return render(request, "ceo/enquirylist.html", context)

@login_required(login_url="/")

def listallproject(request):
    allproject = ProjectStatus.objects.all()
  
    context = {
        "is_enquiryList": True, 
        "allproject": allproject
        }
    return render(request, "ceo/listallproject.html", context)


def clientlist(request):
    clienilist = Client.objects.all()
  
    context = {
        "is_enquiryList": True, 
        "clienilist": clienilist
        }
    return render(request, "ceo/clientlist.html", context)








#################################   pm features  #############################

def enquiryCeo(request):
    enquirylistdata = Enquiry.objects.filter(status="Enquiry")
    context = {
        "enquirylistdata": enquirylistdata,
    }
    return render(request,"ceo/pmfeatures/enquiry.html",context)


def viewenquriesCeo(request, id):
    details = Enquiry.objects.get(id=id)
    forms = PraposalpdfForm(request.POST, request.FILES)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save()
            data.enquiry = details
            data.save()
            Enquiry.objects.filter(id=id).update(status="Added To Proposal")
            return redirect("/enquiry-ceo")
        else:
            pass
    else:
        context = {
            "details": details,
            "forms": forms,
        }
        return render(request, "ceo/pmfeatures/view-enquires.html",context)
    return render(request, "ceo/pmfeatures/view-enquires.html",context)




def proposalCeo(request):
    data = Enquiry.objects.filter(status="Added To Proposal")
    pm = request.user.employee
    context = {
        "is_proposal": True,
        "data": data,
    }
    return render(request, "ceo/pmfeatures/proposal-ceo.html", context)



def unassigneprojectCeo(request):
    # enquirylist = Enquiry.objects.filter(status="Advance Paid").exclude(
    #     type="Graphic Designing"
    # )
    enquirylist = Enquiry.objects.filter(status="Advance Paid")
    context = {
        "is_unassigneproject": True,
        "enquirylist": enquirylist,
    }
    return render(request, "ceo/pmfeatures/un-assigned-project.html", context)


def addprojectCeo(request, id):
    deatils = Enquiry.objects.get(id=id)
    form = ProjectForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            Project.objects.filter(id=data.id).update(enquiry=deatils)
            project = Project.objects.get(id=data.id)
            Enquiry.objects.filter(id=id).update(status="Project Added")
            projectsrs = SRS(project=project)
            projectsrs.save()

            return redirect("/addteam-ceo/" + str(data.id))
        else:
            pass
    else:

        context = {
            "form": form,
        }
        return render(request, "ceo/pmfeatures/addproject-ceo.html", context)
    return render(request, "ceo/pmfeatures/addproject-ceo.html", context)

# http://127.0.0.1:8000/addproject-ceo/1

def addteamCeo(request, id):
    employee = Employees.objects.filter(catagory__catagory__catagory_title="EMPLOYEE")
    context = {
        "employee": employee,
        "id": id,
    }
    return render(request, "ceo/pmfeatures/add-team-ceo.html", context)



def addscheduleCeo(request, id):
    project_obj = Project.objects.get(id=id)
    team_mbr = ProjectMembers.objects.get(project=project_obj)
    mbr = ProjectMembers.objects.filter(project=project_obj)
    if request.method == "POST":
        meetingDate = request.POST["meetingDate"]
        platform = request.POST["platform"]
        time = request.POST["time"]
        link = request.POST["link"]

        meeting = Meeting(
            project=project_obj,
            date=meetingDate,
            time=time,
            platform=platform,
            meeting_link=link,
        )
        meeting.save()
        project_obj.status = "Waiting for SRS"
        project_obj.save()
        return redirect("ceo:ceodashboard")

    context = {
        "team": team_mbr,
        "mbr": mbr,
        "project": project_obj,
        # "members":memberrs,
    }
    return render(request, "ceo/pmfeatures/add-schedule-ceo.html", context)



 # crm

def viewenquiryCeo(request, id):
    details = EnquiryNote.objects.get(id=id)

    context = {"details": details, "id": id}
    return render(request, "ceo/crmfeatures/enquiry-ceo.html", context)



def createProjectCeo(request, id):
    details = EnquiryNote.objects.get(id=id)
    form = EnquiryForm(request.POST, request.FILES)
    form2 = ClientForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            Enquiry.objects.filter(id=data.id).update(Enquirynote=details)
            EnquiryNote.objects.filter(id=id).update(status="DeActivate")
            if data.type == "Graphic Designing":
                print("if")
                Enquiry.objects.filter(id=data.id).update(status="Added To Proposal")
                return redirect("ceo:ceodashboard")
            else:
                print("else")
                return redirect("ceo:ceodashboard")

    context = {"details": details, "form": form, "form2": form2, "id": id}

    return render(request, "ceo/crmfeatures/create_project_ceo.html", context)




    # accounts

def praposalAccountsCeo(request):
    # Enquiry.objects.filter(status='Bill Creation')
    praposallist = Praposalpdf.objects.filter(enquiry__status="Bill Creation")
    # praposallist = Enquiry.objects.filter(status='Bill Creation')
    # print(praposallist,"##"*10)
    context = {"praposallist": praposallist}
    return render(request, "ceo/accounts/proposal-ceo.html", context)


def followuplistceo(request):
    followlist = Enquiry.objects.filter(status="Bill Advance")
    context = {
        "followlist": followlist,
    }
    return render(request, "ceo/accounts/followup-ceo.html", context)




    
    