from django.shortcuts import render
from ceo.models import EmergenctContact, Employees,LeaveRequests,ExcuseRequests,Client
from pm.models import Project
from hrm.form import EmergenctContactForm, EmployeeRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gmanager.decorators import auth_hrm
# Create your views here.

@login_required(login_url='/')
@auth_hrm
def hrmHome(request):
    emp = Employees.objects.all().count()
    project = Project.objects.all().count()
    client = Client.objects.all().count()
    context = {
        "is_hrmHome":True,
        'emp' : emp,
        "project":project,
        "client":client
    }
    return render(request, 'hrm/hrmhome.html',context)


@login_required(login_url='/')
@auth_hrm
def employeeList(request):

    allemp = EmergenctContact.objects.all().order_by('-employee_id')
    empform = EmployeeRegisterForm(request.POST or None, request.FILES or None) 
    empcontactform = EmergenctContactForm(request.POST or None)
    if request.method == 'POST':
        if empform.is_valid() and empcontactform.is_valid():
            empdata = empform.save()            
            form_data = Employees.objects.get(id=empdata.id)
            empcontact = empcontactform.save()
            EmergenctContact.objects.filter(id=empcontact.id).update(employee=form_data)
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,employee=form_data)
        else:
            context={
            "empform" : empform,
            "empcontactform" : empcontactform,
        } 
            return render (request,'hrm/employees.html',context)
    context = {
        "is_employeeList":True,
        "empform" : empform,
        "empcontactform" : empcontactform,
        "allemp" : allemp,
    }
    return render(request, 'hrm/employees.html',context)



@login_required(login_url='/')
@auth_hrm
def clientList(request):
    clienilist=Client.objects.all()
    context = {
        "is_clientList":True,
        "clienilist":clienilist
    }
    return render(request, 'hrm/client.html',context)


@login_required(login_url='/')
@auth_hrm
def leaveRequest(request):
    leave = LeaveRequests.objects.filter(pm_accept = True , status ='Waiting')
    context = {
        "is_leaveRequest":True,
        "leave":leave
    }
    return render(request, 'hrm/leaverequest.html',context)


@login_required(login_url='/')
@auth_hrm
def leaveReport(request):
    context = {
        "is_leaveReport":True,
    }
    return render(request, 'hrm/leavereport.html',context)


@login_required(login_url='/')
@auth_hrm
def attantanceReport(request):
    context = {
        "is_attantanceReport":True,
    }
    return render(request, 'hrm/attantancereport.html',context)


@login_required(login_url='/')
@auth_hrm
def hrsettings(request):
    context = {
        "is_hrsettings":True,
    }
    return render(request, 'hrm/hrsettings.html',context)


@login_required(login_url='/')
@auth_hrm
def attantanceList(request):
    allemp = Employees.objects.all()
    context = {
        "is_attantanceList":True,
        "allemp" : allemp,
    }
    return render(request, 'hrm/attantancelist.html',context)



@csrf_exempt
def hrmaccept(request,id):
    LeaveRequests.objects.filter(id=id).update(hr_accept= True,status='Approved')
    return JsonResponse({'value': 'msg'})




@login_required(login_url='/')
@auth_hrm
def excuse(request):
    listvalue= ExcuseRequests.objects.filter(status = 'Waiting')
    context = {
        "listvalue":listvalue
    }
    return render(request, 'hrm/excuse.html',context)
    



@csrf_exempt
def changevalue(request):
    id=request.POST['EnquaryID']
    ExcuseRequests.objects.filter(id=id).update(status='Approved')
    return JsonResponse({'value': 'msg'})


