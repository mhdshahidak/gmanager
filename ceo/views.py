from django.shortcuts import render

# Create your views here.


def base(request):
    return render (request,'ceo/partials/base.html')





def login(request):
    return render (request,'ceo/login.html')  


def admin(request):
    return render (request,'ceo/dashboard/admin.html')  


def crm(request):
    return render (request,'ceo/dashboard/crm.html')  


def employee(request):
    return render (request,'ceo/dashboard/employee.html')  


def hr(request):
    return render (request,'ceo/dashboard/hr.html')  



def projectmanager(request):
    return render (request,'ceo/dashboard/projectmanager.html')          


def accounts(request):
    return render (request,'ceo/dashboard/accounts.html')  


def gm(request):
    return render (request,'ceo/dashboard/gm.html')    



def employeeprofile(request):
    return render (request,'ceo/employeeprofile.html')    



def departmentwise(request):
    return render (request,'ceo/departmentwise.html')    


 

def employeelist(request):
    return render (request,'ceo/employeelist.html')        


def allstaff(request):
    return render (request,'ceo/allstaff.html')   


def dailychecked(request):
    return render (request,'ceo/dailychecked.html') 


def project(request):
    return render (request,'ceo/project/project.html')    


def projectlist(request):
    return render (request,'ceo/project/projectlist.html')  


def viewproject(request):
    return render (request,'ceo/project/viewproject.html')        
    