from django.shortcuts import render

# Create your views here.

def crmHome(request):
    return render(request,'crm/home.html')

def enquiryList(request):
    return render(request,'crm/enquirylist.html')