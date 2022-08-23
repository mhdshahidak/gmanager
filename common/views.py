from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import *
from django.contrib.auth import get_user_model
from . forms import LeaveRequestsForm, ExcuseRequestsForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def base(request):
    return render(request,'common/partials/base.html')



@login_required(login_url='/')
def leave_application(request):
    user_name = request.user.employee
    leave_form = LeaveRequestsForm(request.POST or None)
    # now_date = datetime.now()
    if request.method == "POST":
        if leave_form.is_valid():           
                data = leave_form.save()            
                LeaveRequests.objects.filter(id=data.id).update(employee=user_name)    
                if request.user.employee.catagory.catagory.catagory_title == "EMPLOYEE":  
                    return redirect('employee:employeehome')
                elif request.user.employee.catagory.catagory.catagory_title == "HRM" :
                    return redirect('hrm:hrhome')
                elif request.user.employee.catagory.catagory.catagory_title == "CRM":
                    return redirect('crm:crmhome')
                elif request.user.employee.catagory.catagory.catagory_title == "PM":
                    return redirect('pm:index')
                elif request.user.employee.catagory.catagory.catagory_title == "GM":
                    return redirect('gm:home')
                elif request.user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
                    return redirect('accounts:home')
                elif request.user.employee.catagory.catagory.catagory_title == "CLIENT":
                    return redirect('clients:home')
                                   
                # return redirect('common:leaveapplication')

        else:
            pass
    # print(user_name)
    context = {
        'user':user_name,
        'leaveform':leave_form,
    }
    return render(request,'common/leave_apply.html', context)

@login_required(login_url='/')
def attendanceRreport(request):
    return render(request,'common/attendance_report.html')

@login_required(login_url='/')
def settings(request):
    return render(request,'common/settings.html')


@login_required(login_url='/')
def leaves(request):
    user_name = request.user.employee
  
    leavelist = LeaveRequests.objects.filter(employee=request.user.employee)
 
    context={
        "user":user_name,
        "leavelist":leavelist
    }

    return render(request,'common/leaves.html',context)

@login_required(login_url='/')
def gohome(request):
    user_name = request.user.employee
    print(user_name)
    if request.user.employee.catagory.catagory.catagory_title == "EMPLOYEE":
        return redirect('employee:employeehome')
    elif request.user.employee.catagory.catagory.catagory_title == "HRM" :
        return redirect('hrm:hrhome')
    elif request.user.employee.catagory.catagory.catagory_title == "CRM":
        return redirect('crm:crmhome')
    elif request.user.employee.catagory.catagory.catagory_title == "PM":
      
        return redirect('pm:index')
    elif request.user.employee.catagory.catagory.catagory_title == "GM":
        return redirect('gm:home')
    elif request.user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
        return redirect('accounts:home')
    elif request.user.employee.catagory.catagory.catagory_title == "CLIENT":
        return redirect('clients:home')    


@login_required(login_url='/')
def excuse(request):
    user_name = request.user.employee
    leaveform = ExcuseRequestsForm(request.POST or None)
    if request.method == "POST":
        if leaveform.is_valid():           
                data = leaveform.save()            
                ExcuseRequests.objects.filter(id=data.id).update(employee=user_name)
                if request.user.employee.catagory.catagory.catagory_title == "EMPLOYEE":  
                    return redirect('employee:employeehome')
                elif request.user.employee.catagory.catagory.catagory_title == "HRM" :
                    return redirect('hrm:hrhome')
                elif request.user.employee.catagory.catagory.catagory_title == "CRM":
                    return redirect('crm:crmhome')
                elif request.user.employee.catagory.catagory.catagory_title == "PM":
                    return redirect('pm:index')
                elif request.user.employee.catagory.catagory.catagory_title == "GM":
                    return redirect('gm:home')
                elif request.user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
                    return redirect('accounts:home')
                elif request.user.employee.catagory.catagory.catagory_title == "CLIENT":
                    return redirect('clients:home')
        else:
            pass        
    context={
        "leaveform":leaveform,
    }
    return render(request,'common/excuse.html',context)
