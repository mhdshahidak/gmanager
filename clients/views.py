from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def base(request):
    return render (request,'clients/partials/base.html')

@login_required(login_url='/')
def home(request):
    return render (request,'clients/index.html')    


@login_required(login_url='/')
def updation(request):
    return render (request,'clients/updation.html')



@login_required(login_url='/')
def payment(request):
    return render (request,'clients/payment.html')    