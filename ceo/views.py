from django.shortcuts import render

# Create your views here.




# def log_in(request):
# if request.method == 'POST':
#     email = request.POST['email']
#     password = request.POST['password']

#     user = authenticate(email=email, password=password)
#     if user is not None:
#         login(request, user)
#         if user.is_superuser == True:
#             return redirect('admins:admindash')
#         elif user.branch != None:
#             return redirect('branch:master')
#         elif user.teacher != None:
#             return redirect('teacher:profile')
#         elif user.Student !=None:
#             return redirect('student:home')
#     else:
#         msg = "* Incorrect email or password *"
#         return render(request,'adminapps/login.html',{'msg':msg,})
# return render(request,'adminapps/login.html')




def base(request):
    return render (request,'ceo/partials/base.html')





def login(request):
    return render (request,'ceo/login.html')  


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
    return render (request,'ceo/allstaff.html')   


def dailychecked(request):
    return render (request,'ceo/dailychecked.html') 


def project(request):
    return render (request,'ceo/project/project.html')    


def projectlist(request):
    return render (request,'ceo/project/projectlist.html')  


def viewproject(request):
    return render (request,'ceo/project/viewproject.html')        
    