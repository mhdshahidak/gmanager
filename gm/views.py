from django.shortcuts import render

# Create your views here.
def base(request):
    return render (request,'gm/partials/base.html')

def home(request):
    return render (request,'gm/home.html')  

def paymentdetails(request):
    return render (request,'gm/paymentdetails.html')  

def viewhistory(request):
    return render (request,'gm/viewhistory.html')  


def salary(request):
    return render (request,'gm/salary.html')  
    