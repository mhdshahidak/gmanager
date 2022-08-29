from django.db.models import Count
from multiprocessing import context
from django.shortcuts import render,redirect
from . models import *
from crm.models import Enquiry
from ceo.models import Employees ,LeaveRequests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . form import PraposalpdfForm,ProjectForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
from pytz import timezone

@login_required(login_url='/')# Create your views here.
def base(request):
    return render (request,'pm/partials/base.html')

@login_required(login_url='/')
def index(request):
    return render (request,'pm/index.html')    


@login_required(login_url='/')
def enquiry(request):
    enquirylistdata = Enquiry.objects.filter(status = 'Enquiry')
    context={
        "enquirylistdata":enquirylistdata
    }
    return render (request,'pm/enquiry/enquiry.html',context)     

@login_required(login_url='/')
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
    return render (request,'pm/enquiry/viewenquries.html') 


@login_required(login_url='/')
def proposal(request):
    data = Enquiry.objects.filter(status = 'Added To Proposal')
    
    context ={
        "data":data,
    }
    return render (request,'pm/proposal.html',context)     



@login_required(login_url='/')
def project(request):
    return render (request,'pm/project/project.html')    

@login_required(login_url='/')
def projectlist(request):
    return render (request,'pm/project/projectlist.html')  

@login_required(login_url='/')
def viewproject(request):
    return render (request,'pm/project/viewproject.html')  

@login_required(login_url='/')
def unassigneproject(request):
    enquirylist = Enquiry.objects.filter(status = 'Advance Paid')
    context={
        "enquirylist":enquirylist,
    }
    return render (request,'pm/project/unassigneproject.html',context)         


@login_required(login_url='/')
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

@login_required(login_url='/')
def addteam(request,id):
    employee = Employees.objects.all()
    context={
        "employee":employee,
        "id":id
    }
    return render (request,'pm/project/addteam.html',context)
@login_required(login_url='/')
def addschedule(request,id):
    project_obj = Project.objects.get(id=id)
    # print(project)    
    team_mbr = ProjectMembers.objects.get(project=project_obj)
    mbr = ProjectMembers.objects.filter(project=project_obj).values('team__name','team__emp_profile')
    if request.method == 'POST':
        # project = request.POST['projectID']
        meetingDate = request.POST['meetingDate']
        platform = request.POST['platform']
        time = request.POST['time']
        link = request.POST['link']

        meeting = Meeting(project=project_obj,date=meetingDate,time=time,platform=platform,meeting_link=link)
        meeting.save()
        project_obj.status = "Meeting Scheduled"
        project_obj.save()
        return redirect('pm:index')
        
    context = {
        "team":team_mbr,
        "mbr":mbr,
        "project":project_obj,
        # "members":memberrs,
    }

    return render (request,'pm/project/addschedule.html',context)    


@login_required(login_url='/')
def meetings(request):
    # project = Project.objects.get(status="Meeting Scheduled")
    meetings = Meeting.objects.filter(project__status="Meeting Scheduled")
    # print(project)
    context = {
        "meetings":meetings,
    }
    return render(request,'pm/meetings.html',context)

@login_required(login_url='/')
def task(request):
    projects = Project.objects.all()
    context = {
        "projects" : projects,
    }
    return render (request,'pm/project/task.html', context)
    

@login_required(login_url='/')
def viewtask(request):
    return render (request,'pm/project/viewtask.html')  


@login_required(login_url='/')
def srs(request):
    viewsrs = SRS.objects.filter(project__status='SRS uploaded')
    context={
        "viewsrs":viewsrs
    }
    return render (request,'pm/project/srs.html',context)  


@login_required(login_url='/')
def fullprojectlist(request):
    return render (request,'pm/project/fullprojectlist.html')  


@login_required(login_url='/')
def dailyprogress(request):
    today = datetime.now().date()
    # projectlists=DailyProgress.objects.filter(date=today).values('project__projectname','project__starteddate','project__endingdate','project__id').annotate(name_count=Count('project__projectname')).exclude(name_count=1)
    projectlists =DailyProgress.objects.filter(date=today).values('project__projectname','project__starteddate','project__endingdate','project__id').order_by('project').distinct()
    print(projectlists,'*'*28)

    context={
        "projectlists":projectlists
    }

    return render (request,'pm/dailyprogress.html',context)    

@login_required(login_url='/')
def viewdailyreport(request,id):
    today = datetime.now().date()
    time = datetime.now().time()
    # now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    # print(now.time)
    print(today,time)
    projectdata = Project.objects.get(id=id)
    morning= DailyProgress.objects.filter(date=today,project=projectdata,status='Morning')
    afternoon= DailyProgress.objects.filter(date=today,project=projectdata,status='Afternoon')
    evening= DailyProgress.objects.filter(date=today,project=projectdata,status='Evening')
   

        
    context={
        "morning":morning,
        "afternoon":afternoon,
        "evening":evening
    }
    return render (request,'pm/viewdailyreport.html',context)  
    

@login_required(login_url='/')
def qcapprovel(request):
    # qcProject = Project.objects.filter(status="")
    context = {
        "is_qcapprovel" : True,
    }
    return render (request,'pm/qcapprovel.html')


@login_required(login_url='/')
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


@csrf_exempt
def srsapprovel(request):
    id=request.POST['EnquaryID']
    Project.objects.filter(id=id).update(status = 'SRS Approved')
    
    proj = Project.objects.get(id=id)
    member = ProjectMembers.objects.get(project=proj)

    new_projectstatus = ProjectStatus(project=proj,member=member)
    new_projectstatus.save()
    addedprogres = DailyProgress(project=proj)
    addedprogres.save()
    return JsonResponse({'message': 'sucesses'}) 




@csrf_exempt
def Changedailyreport(request,id):
    print(id)
    DailyProgress.objects.filter(id=id).update(checked=True)
    return JsonResponse({'message': 'sucesses'}) 

