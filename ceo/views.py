from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from crm.models import EnquiryNote
from pm.models import DailyProgress


import datetime

# from django.contrib.auth import login as auth_login
# Create your views here.
from . form import RegisterForm, editEmployeeForm
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
            elif user.client !=None:
                return redirect('clients:home')
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



@login_required(login_url='/')
def ceodashboard(request):
    return render (request,'ceo/dashboard/admin.html')  

@login_required(login_url='/')
def crm(request):
    if request.method == 'POST':
        print("success")
        instructions = request.POST['instruction']
        print(instructions)

        new_project_note = EnquiryNote(description=instructions)
        new_project_note.save()
        context = {
            "is_home":True,
            
        }
    else: 
        print('#'*10)         
        context = {
            "is_home":True,
            
        }
        return render(request,'crm/home.html',context)
    return render (request,'ceo/dashboard/crm.html')  

@login_required(login_url='/')
def employe(request):
    return render (request,'ceo/dashboard/employee.html')  


# def hr(request):
#     return render (request,'ceo/dashboard/hr.html')  


@login_required(login_url='/')
def projectmanager(request):
    return render (request,'ceo/dashboard/projectmanager.html')          


# def accounts(request):
#     return render (request,'ceo/dashboard/accounts.html')  


# def gm(request):
#     return render (request,'ceo/dashboard/gm.html')    



def employeeprofile(request):
    return render (request,'ceo/employeeprofile.html')    


@login_required(login_url='/')
def departmentwise(request):
    department = SubCatagory.objects.all()
    class cat:
        def __init__(self,title,counts,id) :
            self.title = title
            self.counts = counts
            self.id = id

    estimatelist=[]
    for i in department:
        id=i.id
        emp_count = Employees.objects.filter(catagory=i).count()
        print(emp_count)
        estimatelist.append(cat(i,emp_count,id))
    print(estimatelist)    
    context = {
        "emp_count":estimatelist,
        # "departments":department,
            }
    return render (request,'ceo/departmentwise.html',context)    
        
   

@login_required(login_url='/')
def departmentwiseEmployee(request,id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "category":category,
        "employees":employees
    }
    return render(request,'ceo/departmentwise_employee.html',context)
 

@login_required(login_url='/')
def employeelist(request):
    return render (request,'ceo/employeelist.html')        


@login_required(login_url='/')
def allstaff(request):
    all_emp = Employees.objects.all().order_by('name')
    form=RegisterForm(request.POST or None)    
    if request.method=='POST':        
        if form.is_valid():           
            data = form.save()            
            form_data = Employees.objects.get(id=data.id)
            
            
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,employee=form_data)
            emergecy = EmergenctContact(employee=form_data)
            emergecy.save()

            return redirect('ceo:ceodashboard')
        else:
            pass

    else:
        context={
            "form":RegisterForm,
            "employees":all_emp,
        } 
        return render (request,'ceo/allstaff.html',context)
    return render (request,'ceo/allstaff.html',context)    
        

@login_required(login_url='/')
def editEmployeeDetails(request,id):
    n = Employees.objects.get(id=id)
    if request.method == 'POST':
        form = RegisterForm(request.POST or None, instance=n)
        if form.is_valid():
            data = form.save()
            password_upadte = get_user_model().objects.get(employee=n)
            password_upadte.set_password(data.password)
            password_upadte.save()
            get_user_model().objects.filter(employee=n).update(username=data.username)
            return redirect('ceo:allstaff')
    else:
        form = RegisterForm(request.POST or None, instance=n)
    context = {
        "form":form,
    }
    return render (request,'ceo/edit_employee.html',context)  
       


@login_required(login_url='/')
def dailychecked(request):
    # print(type(datetime))
    # d1 = datetime.datetime.now()
    # print(d1)
    today = datetime.datetime.now()
    print(today.date,'*'*44)
    projectlists =DailyProgress.objects.filter(date=today)
    context ={
        "projectlists":projectlists,
    }
    return render (request,'ceo/dailychecked.html',context) 


@login_required(login_url='/')
def project(request):
    return render (request,'ceo/project/project.html')    


@login_required(login_url='/')
def projectlist(request):
    return render (request,'ceo/project/projectlist.html')  


@login_required(login_url='/')
def viewproject(request):
    return render (request,'ceo/project/viewproject.html')        
    