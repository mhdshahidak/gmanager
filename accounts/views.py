from django.shortcuts import render

# Create your views here.

def base(request):
    return render (request,'accounts/partials/base.html')


def home(request):
    return render (request,'accounts/home.html')


def praposal(request):
    return render (request,'accounts/praposal.html')

def followuplist(request):
    return render (request,'accounts/followuplist.html')


def completed(request):
    return render (request,'accounts/completed.html')   


def updation(request):
    return render (request,'accounts/updation.html')   
    