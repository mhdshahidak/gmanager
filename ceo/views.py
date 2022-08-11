from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
# from django.contrib.auth import login as auth_login
# Create your views here.
from . form import RegisterForm
from . models import *

def base(request):
    return render (request,'ceo/partials/base.html')





def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']    
        user = authenticate(username=username, password=password)       
        if user is not None:            
            login(request, user)
            if user.is_superuser == True:
                return redirect('ceo:ceodashboard')
            elif user.employee.catagory.catagory.catagory_title == "HRM" :
                return redirect('hrm:hrhome')
            elif user.employee.catagory.catagory.catagory_title == "CRM":
                return redirect('crm:crmhome')
            elif user.employee.catagory.catagory.catagory_title == "PM":
                return redirect('pm:index')
            elif user.employee.catagory.catagory.catagory_title == "GM":
                return redirect('gm:home')
            elif user.employee.catagory.catagory.catagory_title == "ACCOUNTS":
                return redirect('accounts:home')
            elif user.employee.catagory.catagory.catagory_title == "CLIENT":
                return redirect('clients:home')
            elif user.employee.catagory.catagory.catagory_title == "EMPLOYEE":
                return redirect('employee:employeehome')
            
        else:
        
            context = {
                "status":1,               
            }
            return render(request,'ceo/login.html',context)
    
    return render (request,'ceo/login.html')  


def logout_view(request):
    logout(request)
    return redirect('ceo:login')




def ceodashboard(request):
    return render (request,'ceo/dashboard/admin.html')  


def crm(request):
    return render (request,'ceo/dashboard/crm.html')  


def employe(request):
    return render (request,'ceo/dashboard/employee.html')  


# def hr(request):
#     return render (request,'ceo/dashboard/hr.html')  



def projectmanager(request):
    return render (request,'ceo/dashboard/projectmanager.html')          


# def accounts(request):
#     return render (request,'ceo/dashboard/accounts.html')  


# def gm(request):
#     return render (request,'ceo/dashboard/gm.html')    



def employeeprofile(request):
    return render (request,'ceo/employeeprofile.html')    



def departmentwise(request):
    return render (request,'ceo/departmentwise.html')    


 

def employeelist(request):
    return render (request,'ceo/employeelist.html')        


def allstaff(request):
    form=RegisterForm(request.POST or None)    
    if request.method=='POST':        
        if form.is_valid():           
            data = form.save()            
            form_data = Employees.objects.get(id=data.id)
            
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,employee=form_data)

            return redirect('ceo:ceodashboard')
        else:
            pass

    else:
        context={
            "form":RegisterForm,
        } 
        return render (request,'ceo/allstaff.html',context)
    return render (request,'ceo/allstaff.html',context)    
        
       
       


def dailychecked(request):
    return render (request,'ceo/dailychecked.html') 


def project(request):
    return render (request,'ceo/project/project.html')    


def projectlist(request):
    return render (request,'ceo/project/projectlist.html')  


def viewproject(request):
    return render (request,'ceo/project/viewproject.html')        
    