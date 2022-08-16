from multiprocessing import context
from django.shortcuts import render,redirect
from . models import *
from crm.models import Enquiry
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . form import PraposalpdfForm
# Create your views here.
def base(request):
    return render (request,'pm/partials/base.html')


def index(request):
    return render (request,'pm/index.html')    



def enquiry(request):
    enquirylistdata = Enquiry.objects.filter(status = 'Enquiry')
    context={
        "enquirylistdata":enquirylistdata
    }
    return render (request,'pm/enquiry/enquiry.html',context)     


def viewenquries(request,id):
    details = Enquiry.objects.get(id=id)
    forms=PraposalpdfForm(request.POST,request.FILES)
    if request.method == 'POST': 
        # print (form.errors) 
        if forms.is_valid():
            print (forms.errors) 
            data = forms.save()
            data.enquiry=details
            data.save()
            Enquiry.objects.filter(id=id).update(status = 'Added To Proposal')
            return redirect('/pm/proposal')
        else:
            pass 
    else:

        context={
        "details":details ,
        "forms":forms
        }
        return render (request,'pm/enquiry/viewenquries.html',context) 
    return render (request,'pm/enquiry/viewenquries.html',context) 



def proposal(request):
    data = Enquiry.objects.filter(status = 'Added To Proposal')
    
    context ={
        "data":data,
    }
    return render (request,'pm/proposal.html',context)     




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



def srs(request):
    return render (request,'pm/project/srs.html')  



def fullprojectlist(request):
    return render (request,'pm/project/fullprojectlist.html')  



def dailyprogress(request):
    return render (request,'pm/dailyprogress.html')    


def viewdailyreport(request):
    return render (request,'pm/viewdailyreport.html')  
    


def qcapprovel(request):
    return render (request,'pm/qcapprovel.html')  

def leaverequest(request):
    return render (request,'pm/leaverequest.html')    
    

@csrf_exempt
def changeStatus(request):
    id=request.POST['EnquaryID']
    Enquiry.objects.filter(id=id).update(status = 'Added To Proposal')

    return JsonResponse({'message': 'sucesses'}) 

@csrf_exempt
def savaProposal(request):
    id=request.POST['EnquaryID']
    Enquiry.objects.filter(id=id).update(status = 'Bill Creation')
    return JsonResponse({'message': 'sucesses'}) 


@csrf_exempt
def rejectedreason(request,id):
    details=Enquiry.objects.get(id=id)
    
    data={
        "id":details.id,
    }
    return JsonResponse({'value': data})

@csrf_exempt
def typereason(request):
    id=request.POST['id']
    typereason=request.POST['reason']
    Enquiry.objects.filter(id=id).update(status='Rejected',reason=typereason)
    return JsonResponse({'value': 'msg'})

