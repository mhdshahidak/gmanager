from multiprocessing import context
from django.shortcuts import render,redirect
from . models import *
from crm.models import Enquiry
from ceo.models import Employees ,LeaveRequests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . form import PraposalpdfForm,ProjectForm


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
    enquirylist = Enquiry.objects.filter(status = 'Advance Paid')
    context={
        "enquirylist":enquirylist,
    }
    return render (request,'pm/project/unassigneproject.html',context)         



def addproject(request,id):
    deatils= Enquiry.objects.get(id=id)
    form=ProjectForm(request.POST)
    if request.method == 'POST': 
        # print (form.errors) 
        if form.is_valid():
            print (form.errors) 
            data = form.save()
            Project.objects.filter(id=data.id).update(enquiry=deatils)
            return redirect('/pm/addteam/'+str(data.id))
        else:
            pass 
    else:

        context={
       
        "form":form
        }
        return render (request,'pm/project/addproject.html',context)
    return render (request,'pm/project/addproject.html',context)  


def addteam(request,id):
    employee = Employees.objects.all()
    context={
        "employee":employee,
        "id":id
    }
    return render (request,'pm/project/addteam.html',context)

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
    leave = LeaveRequests.objects.filter(pm_accept = False , status ='Waiting')
    print(leave)
    context={
        "leave":leave
    }
    return render (request,'pm/leaverequest.html',context)    
    

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



@csrf_exempt
def leadersearch(request):
    employeename=request.POST['employee']
    projectid=request.POST['projectid']
    enqid = Project.objects.get(id=projectid)

    # print(employeename)
    details=Employees.objects.get(name=employeename)
    member_obj = ProjectMembers(project=enqid,lead=details)
    member_obj.save()
    
    
    data={
        "id":details.id,
        "name":details.name,
        "member":member_obj.id,
       
        
    }
    
    
    print(data)
    return JsonResponse({'value': data})





@csrf_exempt
def membersearch(request):
    employeename=request.POST['member']
    leaderid=request.POST['leaderid']
    employee_prjt = request.POST['memberObj']
    projectid = request.POST['projectid']


     
    details=Employees.objects.get(name=employeename)
    member_prjct_obj = ProjectMembers.objects.get(id=employee_prjt)
    member_prjct_obj.team.add(details)
    # projectId = Project.objects.filter(id=projectid).update(status = "Team Ass")




    
    
    data={
        "id":details.id,
        "name":details.name,
        "catagory":details.catagory.title,

        
    }
    
   
    print(data)
    return JsonResponse({'value': data})    


@csrf_exempt
def viedetails(request,id):
    getdata =  LeaveRequests.objects.get(id=id)
    data ={
        'leave_type':getdata.leave_type,
        'aply_date':getdata.aply_date,
        'from_date':getdata.from_date,
        'to_date':getdata.to_date,
        'no_days':getdata.no_days,
        'reason':getdata.reason,
        
    }
    print(data)
    return JsonResponse({'value': data})

@csrf_exempt
def acceptdeatils(request,id):
    LeaveRequests.objects.filter(id=id).update(pm_accept= True)
    return JsonResponse({'value': 'msg'})

@csrf_exempt
def rejectdeatils(request,id):
    getdata=LeaveRequests.objects.get(id=id)
    data ={
        'id':getdata.id,
    }
    return JsonResponse({'value':data})


@csrf_exempt
def reason(request):
    id=request.POST['id']
    rejectedreason=request.POST['rejectedreason']
    LeaveRequests.objects.filter(id=id).update(rejected_reason=rejectedreason,status='Rejected')
    return JsonResponse({'value': 'msg'})    