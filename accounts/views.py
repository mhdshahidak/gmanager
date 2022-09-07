from multiprocessing import context
from django.shortcuts import render,redirect
from crm.models import Enquiry
from pm.models import Praposalpdf

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gmanager.decorators import auth_accounts
# Create your views here.

def base(request):
    return render (request,'accounts/partials/base.html')


@login_required(login_url='/')
@auth_accounts
def home(request):
    createqotation = Enquiry.objects.filter(status='Bill Creation').count()
    pendingadvance = Enquiry.objects.filter(status = 'Bill Advance').count()

    context={
        "createqotation":createqotation,
        "pendingadvance":pendingadvance,
    }
    return render (request,'accounts/home.html',context)


@login_required(login_url='/')
@auth_accounts
def praposal(request):

    praposallist= Praposalpdf.objects.filter(enquiry__status='Bill Creation')
    # praposallist = Enquiry.objects.filter(status='Bill Creation')
    context = {
        "praposallist":praposallist
    }
    return render (request,'accounts/praposal.html',context)

@login_required(login_url='/')
@auth_accounts
def followuplist(request):
    followlist = Enquiry.objects.filter(status = 'Bill Advance')

    context ={
        "followlist":followlist
    }
    return render (request,'accounts/followuplist.html',context)


@login_required(login_url='/')
@auth_accounts
def completed(request):
    return render (request,'accounts/completed.html')   


@login_required(login_url='/')
@auth_accounts
def updation(request):
    return render (request,'accounts/updation.html')   
    




@csrf_exempt
def changebill(request):
    id=request.POST['EnquaryID']
    Enquiry.objects.filter(id=id).update(status = 'Bill Advance')
    return JsonResponse({'message': 'sucesses'}) 
    
@csrf_exempt
def changefollow(request):
    id=request.POST['EnquaryID']
    Enquiry.objects.filter(id=id).update(status = 'Advance Paid')
    return JsonResponse({'message': 'sucesses'}) 

    