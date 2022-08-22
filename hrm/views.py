from django.shortcuts import render
from ceo.models import EmergenctContact, Employees,LeaveRequests,ExcuseRequests

from hrm.form import EmergenctContactForm, EmployeeRegisterForm

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def hrmHome(request):
    emp = Employees.objects.all().count()
    context = {
        "is_hrmHome":True,
        'emp' : emp,
    }
    return render(request, 'hrm/hrmhome.html',context)


def employeeList(request):

    allemp = EmergenctContact.objects.all().order_by('-employee_id')
    empform = EmployeeRegisterForm(request.POST or None, request.FILES or None) 
    empcontactform = EmergenctContactForm(request.POST or None)
    if request.method == 'POST':
        if empform.is_valid() and empcontactform.is_valid():
            print(empcontactform.errors)
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



def clientList(request):
    context = {
        "is_clientList":True,
    }
    return render(request, 'hrm/client.html',context)


def leaveRequest(request):
    leave = LeaveRequests.objects.filter(pm_accept = True , status ='Waiting')
    context = {
        "is_leaveRequest":True,
        "leave":leave
    }
    return render(request, 'hrm/leaverequest.html',context)


def leaveReport(request):
    context = {
        "is_leaveReport":True,
    }
    return render(request, 'hrm/leavereport.html',context)


def attantanceReport(request):
    context = {
        "is_attantanceReport":True,
    }
    return render(request, 'hrm/attantancereport.html',context)


def hrsettings(request):
    context = {
        "is_hrsettings":True,
    }
    return render(request, 'hrm/hrsettings.html',context)


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


