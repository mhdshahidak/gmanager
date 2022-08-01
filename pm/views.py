from django.shortcuts import render

# Create your views here.
def base(request):
    return render (request,'pm/partials/base.html')


def index(request):
    return render (request,'pm/index.html')    



def enquiry(request):
    return render (request,'pm/enquiry/enquiry.html')     


def viewenquries(request):
    return render (request,'pm/enquiry/viewenquries.html')     