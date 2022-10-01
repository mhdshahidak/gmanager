from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from ceo.models import (
    Attendence,
    Client,
    EmergenctContact,
    Employees,
    ExcuseRequests,
    LeaveRequests,
    TeamCategory,
    TeamMembers,
)
from gmanager.decorators import auth_hrm
from hrm.form import EmergenctContactForm, EmployeeRegisterForm
from pm.models import Project

# Create your views here.


@login_required(login_url="/")
@auth_hrm
def hrmHome(request):
    emp = Employees.objects.all().count()
    project = Project.objects.all().count()
    client = Client.objects.all().count()
    leave = LeaveRequests.objects.filter(pm_accept=True, status="Waiting").count()
    listvalue = ExcuseRequests.objects.filter(status="Waiting").count()
    context = {
        "is_hrmHome": True,
        "emp": emp,
        "project": project,
        "client": client,
        "leave": leave,
        "listvalue": listvalue,
    }
    return render(request, "hrm/hrmhome.html", context)


@login_required(login_url="/")
@auth_hrm
def employeeList(request):

    allemp = EmergenctContact.objects.all().order_by("-employee_id")
    empform = EmployeeRegisterForm(request.POST or None, request.FILES or None)
    empcontactform = EmergenctContactForm(request.POST or None)
    if request.method == "POST":
        if empform.is_valid() and empcontactform.is_valid():
            empdata = empform.save()
            form_data = Employees.objects.get(id=empdata.id)
            empcontact = empcontactform.save()
            EmergenctContact.objects.filter(id=empcontact.id).update(employee=form_data)
            User = get_user_model()
            User.objects.create_user(
                username=form_data.username,
                password=form_data.password,
                employee=form_data,
            )
            return redirect("/hrm/employees")
        else:
            context = {
                "empform": empform,
                "empcontactform": empcontactform,
            }
            return render(request, "hrm/employees.html", context)
    context = {
        "is_employeeList": True,
        "empform": empform,
        "empcontactform": empcontactform,
        "allemp": allemp,
    }
    return render(request, "hrm/employees.html", context)


@login_required(login_url="/")
@auth_hrm
def clientList(request):
    clienilist = Client.objects.all()
    context = {"is_clientList": True, "clienilist": clienilist}
    return render(request, "hrm/client.html", context)


@login_required(login_url="/")
@auth_hrm
def leaveRequest(request):
    leave = LeaveRequests.objects.filter(pm_accept=True, status="Waiting")
    context = {"is_leaveRequest": True, "leave": leave}
    return render(request, "hrm/leaverequest.html", context)


@login_required(login_url="/")
@auth_hrm
def leaveReport(request):
    context = {
        "is_leaveReport": True,
    }
    return render(request, "hrm/leavereport.html", context)


@login_required(login_url="/")
@auth_hrm
def team(request):
    lisatteam = TeamCategory.objects.all()

    if request.method == "POST":
        teamname = request.POST["teamname"]
        namesave = TeamCategory(teamname=teamname)
        namesave.save()
        return redirect("/hrm/team")

    context = {"is_team": True, "lisatteam": lisatteam}
    return render(request, "hrm/team.html", context)


@login_required(login_url="/")
@auth_hrm
def addteam(request, id):
    catid = TeamCategory.objects.get(id=id)

    members = TeamMembers.objects.filter(teamname=catid)
    employee = Employees.objects.all()
    if request.method == "POST":
        employees = request.POST["employees"]
        employeeid = Employees.objects.get(name=employees)
        savemember = TeamMembers(teamname=catid, employee=employeeid)
        savemember.save()
        return redirect("/hrm/addteam/" + id)
    context = {"is_attantanceReport": True, "employee": employee, "members": members}
    return render(request, "hrm/addteam.html", context)


@login_required(login_url="/")
@auth_hrm
def attantanceReport(request):
    if request.method == "POST":
        serachdate = request.POST["serachdate"]
        print(serachdate, "*" * 7)
        serachdate = request.POST["serachdate"]
        if Attendence.objects.filter(date=serachdate).exists():
            print("exist")
            presentdate = Attendence.objects.filter(status="Present").count()
            absentdate = Attendence.objects.filter(status="Leave").count()
            print(presentdate, absentdate)
            employeedetails = Attendence.objects.filter(date=serachdate).all()

            context = {
                "is_attantanceReport": True,
                "presentdate": presentdate,
                "absentdate": absentdate,
                "employeedetails": employeedetails,
                "status": 0,
            }
            return render(request, "hrm/attantancereport.html", context)

        else:
            context = {"status": 1}
            return render(request, "hrm/attantancereport.html", context)
    context = {
        "is_attantanceReport": True,
    }
    return render(request, "hrm/attantancereport.html", context)


@login_required(login_url="/")
@auth_hrm
def hrsettings(request):
    context = {
        "is_hrsettings": True,
    }
    return render(request, "hrm/hrsettings.html", context)


@login_required(login_url="/")
@auth_hrm
def attantanceList(request):
    allemp = Employees.objects.all()
    if request.method == "POST":
        attendence = request.POST.getlist("attendence[]")
        date = request.POST["date"]
        punchin = request.POST["punchin"]
        punchout = request.POST["punchout"]
        Employeeid = request.POST["Employeeid"]
        employdata = Employees.objects.get(id=Employeeid)
        saveattendence = Attendence(
            employee=employdata, date=date, punch_intime=punchin, punch_outtime=punchout
        )
        saveattendence.save()
        print(len(attendence))
        if len(attendence) == 1:
            for i in enumerate(attendence):
                print(i)
                if i[1] == "Morning":
                    print("morning")
                    Attendence.objects.filter(id=saveattendence.id).update(morning=True)
                    return redirect("/hrm/attantancelist")

                elif i[1] == "Afternoon":
                    print("Afternoon")
                    Attendence.objects.filter(id=saveattendence.id).update(evening=True)
                    return redirect("/hrm/attantancelist")

                else:
                    print("dfvsfvbgf", "@" * 10)
        elif len(attendence) == 2:
            print("BOTH WORKING", "$" * 10)
            Attendence.objects.filter(id=saveattendence.id).update(
                morning=True, evening=True
            )
            return redirect("/hrm/attantancelist")
        else:
            return redirect("/hrm/attantancelist")

    context = {
        "is_attantanceList": True,
        "allemp": allemp,
    }
    return render(request, "hrm/attantancelist.html", context)


def leave(request):
    if request.method == "POST":
        date = request.POST["date"]
        Employeeid = request.POST["idleave"]
        employdata = Employees.objects.get(id=Employeeid)
        saveattendence = Attendence(employee=employdata, date=date, status="Leave")
        saveattendence.save()
        return redirect("/hrm/attantancelist")


@csrf_exempt
def hrmaccept(request, id):
    LeaveRequests.objects.filter(id=id).update(hr_accept=True, status="Approved")
    return JsonResponse({"value": "msg"})


@login_required(login_url="/")
@auth_hrm
def excuse(request):
    listvalue = ExcuseRequests.objects.filter(status="Waiting")
    context = {"listvalue": listvalue}
    return render(request, "hrm/excuse.html", context)


@csrf_exempt
def changevalue(request):
    id = request.POST["EnquaryID"]
    ExcuseRequests.objects.filter(id=id).update(status="Approved")
    return JsonResponse({"value": "msg"})


@csrf_exempt
def getemployeedata(request, id):
    details = Employees.objects.get(id=id)

    data = {
        "id": details.id,
        "name": details.name,
        "employeeid": details.employee_id,
        "catagory": details.catagory.title,
    }
    return JsonResponse({"value": data})


@csrf_exempt
def getemployeeleave(request, id):
    details = Employees.objects.get(id=id)
    print(details)

    data = {
        "id": details.id,
        "name": details.name,
        "employeeid": details.employee_id,
        "catagory": details.catagory.title,
    }
    return JsonResponse({"value": data})


@csrf_exempt
def addingattendence(request):
    # choice=request.POST['selected_checkboxes']
    # print(choice)

    pass


def employeedetails(request, id):
    details = Employees.objects.get(id=id)
    emergency = EmergenctContact.objects.get(employee=details)
    # project = ProjectMembers.objects.get(team=details)
    data = {
        "name": details.name,
        "catagory": details.catagory.title,
        "employee_id": details.employee_id,
        "email": details.email,
        "dob": details.dob,
        "address": details.address,
        "emp_profile": details.emp_profile.url,
        "phone": details.phone,
        "whatsapp_number": details.whatsapp_number,
        "join_date": details.join_date,
        "district": details.district,
        "state": details.state,
        "nationality": details.nationality,
        "marital_status": details.marital_status,
        "username": details.username,
        "password": details.password,
        "emergency_number": emergency.emergency_number,
        "primarycontact_name": emergency.primarycontact_name,
        "relation": emergency.relation,
    }
    return JsonResponse({"value": data})


def deleteemployee(request, id):
    Employees.objects.get(id=id).delete()
    return redirect("/hrm/employees")


def editemployee(request, id):
    n = Employees.objects.get(id=id)
    emergency = EmergenctContact.objects.get(employee=n)
    empform = EmployeeRegisterForm(
        request.POST or None, request.FILES or None, instance=n
    )
    empcontactform = EmergenctContactForm(request.POST or None, instance=emergency)
    if request.method == "POST" or "FILES":
        print("post worked")
        print(empform.errors)
        if empform.is_valid() and empcontactform.is_valid():
            print(empform.errors)
            print("valid")
            data = empform.save()
            empcontactform.save()
            password_upadte = get_user_model().objects.get(employee=n)
            password_upadte.set_password(data.password)
            password_upadte.save()
            get_user_model().objects.filter(employee=n).update(username=data.username)
            return redirect("hrm:employees")
        else:
            print("not valid")
    else:
        print("else worked")
        empform = EmployeeRegisterForm(
            request.POST or None, request.FILES or None, instance=n
        )
        empcontactform = EmergenctContactForm(request.POST or None, instance=emergency)
        context = {"empform": empform, "empcontactform": empcontactform}
        return render(request, "hrm/editemployee.html", context)
    print("not worked")
    context = {"empform": empform, "empcontactform": empcontactform}
    return render(request, "hrm/editemployee.html", context)


@csrf_exempt
def checkexist(request):
    check_name = request.POST["checkname"]
    object = Employees.objects.filter(username=check_name).exists()
    return JsonResponse({"IsExist": object})
