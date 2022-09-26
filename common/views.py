from collections import ChainMap
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import *
from django.contrib.auth import get_user_model
from . forms import ChangePasswordForm, EmergenctResetForm, LeaveRequestsForm, ExcuseRequestsForm, ProfileResetForm
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
    userdetails=Employees.objects.get(id=request.user.employee.id)
    emergency = EmergenctContact.objects.get(employee=userdetails)
    print(userdetails)
    if request.method =='POST':
        name = request.POST['name']
        pic =request.FILES.get('pic', "New default that isn't None")
        print(pic)
        email = request.POST['email']
        phone = request.POST['phone']
        whatsapp = request.POST['whatsapp']
        emgname = request.POST['emgname']
        emgnumber = request.POST['emgnumber']
        emgrelation = request.POST['emgrelation']
        if pic == "New default that isn't None":
            print('if worked')
            Employees.objects.filter(id=request.user.employee.id).update(name=name, phone=phone, email=email, whatsapp_number=whatsapp)
            EmergenctContact.objects.filter(employee=userdetails).update(emergency_number=emgnumber, primarycontact_name=emgname,relation=emgrelation )
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
            print('else worked')
            Employees.objects.filter(id=request.user.employee.id).update(name=name, phone=phone, email=email, whatsapp_number=whatsapp)
            obj=Employees.objects.get(id=request.user.employee.id)
            obj.emp_profile=pic
            obj.save()
            EmergenctContact.objects.filter(employee=userdetails).update(emergency_number=emgnumber, primarycontact_name=emgname,relation=emgrelation )
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
        context={
            "userdetails":userdetails,
            "emergency":emergency,
        }
        return render (request,'common/settings.html',context)
# <<<<<<< HEAD
#     change_form = ChangePasswordForm(request.POST or None)
#     # now_date = datetime.now()
#     # if request.method == "POST":
#     #     if change_form.is_valid():           
#     #         data = change_form.save() 
#     # user_name = request.user.employee.catagory.catagory.catagory_title
#     # print(user_name,'%'*56)
# =======
#     user_name = request.user.employee.catagory.catagory.catagory_title

# >>>>>>> 09d27a103151de39ac14138296195c96bf396735
    # n = Employees.objects.get(id=request.user.employee.id)
    # print(n)
    # m= EmergenctContact.objects.get(employee=n)
    # if request.method == 'POST':
    #     empform = ProfileResetForm(request.POST or None, request.FILES or None, instance=n) 
    #     empcontactform = EmergenctResetForm(request.POST or None,instance=m)

    #     if empform.is_valid() and empcontactform.is_valid():
    #         empdata = empform.save()            
    #         form_data = Employees.objects.get(id=empdata.id)
    #         empcontact = empcontactform.save()
    #         EmergenctContact.objects.filter(id=empcontact.id).update(employee=form_data)

    #         password_upadte = get_user_model().objects.get(employee=n)
    #         password_upadte.set_password(form_data.password)
    #         password_upadte.save()
    #         get_user_model().objects.filter(employee=n).update(username=form_data.username)
    #         if request.user.employee.catagory.catagory.catagory_title == "EMPLOYEE":  
    #             return redirect('employee:employeehome')
    #         elif request.user.employee.catagory.catagory.catagory_title == "HRM" :
    #             return redirect('hrm:hrhome')
    #         elif request.user.employee.catagory.catagory.catagory_title == "CRM":
    #             return redirect('crm:crmhome')
    #         elif request.user.employee.catagory.catagory.catagory_title == "PM":
    #             return redirect('pm:index')
    #         elif request.user.employee.catagory.catagory.catagory_title == "GM":
    #             return redirect('gm:home')
    #         elif request.user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
    #             return redirect('accounts:home')
    #         elif request.user.employee.catagory.catagory.catagory_title == "CLIENT":
    #             return redirect('clients:home')
            
    #         User = get_user_model()
    #         User.objects.create_user(username=form_data.username, password=form_data.password,employee=form_data)
    # else:
    #     empform = ProfileResetForm(request.POST or None, request.FILES or None, instance=n) 
    #     empcontactform = EmergenctResetForm(request.POST or None,instance=m)
    # context={
    #     "empform" : empform,
    #     "empcontactform" : empcontactform,
    #     # "change_form":change_form
    # } 
    # return render (request,'common/settings.html',context)
    


@login_required(login_url='/')
def leaves(request):
    user_name = request.user.employee
  
    leavelist = LeaveRequests.objects.filter(employee=request.user.employee)
 
    context={
        "user":user_name,
        "leavelist":leavelist
    }

    return render(request,'common/leaves.html',context)

def gohome(request):
    user_name = request.user.employee
 
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
