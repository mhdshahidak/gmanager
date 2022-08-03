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



def proposal(request):
    return render (request,'pm/proposal.html')     




def project(request):
    return render (request,'pm/project/project.html')    


def projectlist(request):
    return render (request,'pm/project/projectlist.html')  


def viewproject(request):
    return render (request,'pm/project/viewproject.html')  


def unassigneproject(request):
    return render (request,'pm/project/unassigneproject.html')         


def addschedule(request):
    return render (request,'pm/project/addschedule.html')    



def task(request):
    return render (request,'pm/project/task.html')
    


def viewtask(request):
    return render (request,'pm/project/viewtask.html')  


def dailyprogress(request):
    return render (request,'pm/dailyprogress.html')    


def viewdailyreport(request):
    return render (request,'pm/viewdailyreport.html')  
    


def qcapprovel(request):
    return render (request,'pm/qcapprovel.html')  
    
    