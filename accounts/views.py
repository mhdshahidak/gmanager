from multiprocessing import context
from django.shortcuts import render,redirect
from crm.models import Enquiry
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

def base(request):
    return render (request,'accounts/partials/base.html')


@login_required(login_url='/')
def home(request):
    return render (request,'accounts/home.html')


@login_required(login_url='/')
def praposal(request):
    praposallist = Enquiry.objects.filter(status='Bill Creation')
    context = {
        "praposallist":praposallist
    }
    return render (request,'accounts/praposal.html',context)

@login_required(login_url='/')
def followuplist(request):
    followlist = Enquiry.objects.filter(status = 'Bill Advance')

    context ={
        "followlist":followlist
    }
    return render (request,'accounts/followuplist.html',context)


@login_required(login_url='/')
def completed(request):
    return render (request,'accounts/completed.html')   


@login_required(login_url='/')
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

    