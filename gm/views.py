

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def base(request):
    return render (request,'gm/partials/base.html')



@login_required(login_url='/')
def home(request):
    return render (request,'gm/home.html')  



@login_required(login_url='/')
def paymentdetails(request):
    return render (request,'gm/paymentdetails.html')  



@login_required(login_url='/')
def viewhistory(request):
    return render (request,'gm/viewhistory.html')  




@login_required(login_url='/')
def salary(request):
    return render (request,'gm/salary.html')  
    

@login_required(login_url='/')
def projectlist(request):
    return render (request,'gm/projectlist.html')  
        