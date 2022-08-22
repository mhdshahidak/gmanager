from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

from crm.models import EnquiryNote
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
        
   

def departmentwiseEmployee(request,id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "category":category,
        "employees":employees
    }
    return render(request,'ceo/departmentwise_employee.html',context)
 

def employeelist(request):
    return render (request,'ceo/employeelist.html')        


def allstaff(request):
    all_emp = Employees.objects.all().order_by('name')
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
            "employees":all_emp,
        } 
        return render (request,'ceo/allstaff.html',context)
    return render (request,'ceo/allstaff.html',context)    
        

def editEmployeeDetails(request,id):
    n = Employees.objects.get(id=id)
    if request.method == 'POST':
        form = RegisterForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('View_Vaccine')
    else:
        form = RegisterForm(request.POST or None, instance=n)
    return render (request,'ceo/allstaff.html',{'form':form,})  
       


def dailychecked(request):
    return render (request,'ceo/dailychecked.html') 


def project(request):
    return render (request,'ceo/project/project.html')    


def projectlist(request):
    return render (request,'ceo/project/projectlist.html')  


def viewproject(request):
    return render (request,'ceo/project/viewproject.html')        
    