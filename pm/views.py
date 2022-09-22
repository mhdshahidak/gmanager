from django.db.models import Count
from multiprocessing import context
from django.shortcuts import render,redirect
from . models import *
from crm.models import Enquiry,EnquiryNote
from ceo.models import Employees ,LeaveRequests,SubCatagory
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . form import PraposalpdfForm,ProjectForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
from pytz import timezone
from django.db.models import Q
from gmanager.decorators import auth_pm
from django.contrib.auth import get_user_model
from crm.form import ClientForm
# Create your views here.
@login_required(login_url='/')
@auth_pm
def base(request):
    return render (request,'pm/partials/base.html')

@login_required(login_url='/')
@auth_pm
def index(request):
    pm = request.user.employee
    enquirylist = EnquiryNote.objects.filter(status = 'Active').count()
    addedtoprop = Enquiry.objects.filter(status = 'Added To Proposal').count()
    billcreation = Enquiry.objects.filter(status = 'Bill Creation').count()
    billadvance = Enquiry.objects.filter(status = 'Bill Advance').count()
    advancepaid = Enquiry.objects.filter(status = 'Advance Paid').count()
    rejected = Enquiry.objects.filter(status = 'Rejected').count()
    enquirylistcount = Enquiry.objects.filter(status = 'Enquiry').count()
    # waitforqc = Project.objects.filter(status="Qc").count()
    enquirylistdata = Enquiry.objects.filter(status = 'Enquiry')
    leavecount = LeaveRequests.objects.filter(pm_accept=False,status="Waiting").count()
    notstated =ProjectStatus.objects.filter(status = 'Not Started').count()
    ongoing =ProjectStatus.objects.filter(status = 'On Going').count()
    onscheduling =ProjectStatus.objects.filter(status = 'On Scheduling').count()
    delayed =ProjectStatus.objects.filter(status = 'Delayed').count()
    waitforqc =ProjectStatus.objects.filter(status = 'Qc').count()
    w4c =ProjectStatus.objects.filter(status = 'W4C').count()
    rework =ProjectStatus.objects.filter(status = 'Rework').count()
    completed =ProjectStatus.objects.filter(status = 'Completed').count()
    srs=SRS.objects.filter(project__status='SRS uploaded').count()
    
    context={
        "is_pmindex":True,
        "pm":pm,
        "enquirylistcount":enquirylistcount,
        "addedtoprop":addedtoprop,
        "billcreation":billcreation,
        "billadvance":billadvance,
        "advancepaid":advancepaid,
        "rejected":rejected,
        "enquirylist":enquirylist,
        "enquirylistdata":enquirylistdata,
        "waitforqc":waitforqc,
        "leavecount":leavecount,
        "srs":srs,
        "notstated":notstated,
        "ongoing":ongoing,
        "onscheduling":onscheduling,
        "delayed":delayed,
        "w4c":w4c,
        "rework":rework,
         "completed":completed,

    }
    return render (request,'pm/index.html',context)    



@login_required(login_url='/')
@auth_pm
def enquiry(request):
    pm = request.user.employee
    enquirylistdata = Enquiry.objects.filter(status = 'Enquiry')
    context={
        "is_enquiry":True,
        "pm":pm,
        "enquirylistdata":enquirylistdata
    }
    return render (request,'pm/enquiry/enquiry.html',context)     



@login_required(login_url='/')
@auth_pm
def viewenquries(request,id):
    pm = request.user.employee
    details = Enquiry.objects.get(id=id)
    forms=PraposalpdfForm(request.POST,request.FILES)
    if request.method == 'POST': 
        if forms.is_valid():
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
        "forms":forms,
        "pm":pm,
        }
        return render (request,'pm/enquiry/viewenquries.html',context) 
    return render (request,'pm/enquiry/viewenquries.html') 




@login_required(login_url='/')
@auth_pm
def proposal(request):
    data = Enquiry.objects.filter(status = 'Added To Proposal')
    pm = request.user.employee
    context ={
        "is_proposal":True,
        "data":data,
        "pm":pm,
    }
    return render (request,'pm/proposal.html',context)     



@login_required(login_url='/')
@auth_pm
def project(request):
    pm = request.user.employee
    context = {
        "is_project":True,
        "pm":pm,
    }
    return render (request,'pm/project/project.html',context)    



@login_required(login_url='/')
@auth_pm
def projectlist(request):
    pm = request.user.employee
    context = {
        "is_projectlist":True,
        "pm":pm,
    }
    return render (request,'pm/project/projectlist.html',context)  



@login_required(login_url='/')
@auth_pm
def viewproject(request):
    return render (request,'pm/project/viewproject.html')  



@login_required(login_url='/')
@auth_pm
def unassigneproject(request):
    pm = request.user.employee
    enquirylist = Enquiry.objects.filter(status = 'Advance Paid')
    context={
        "is_unassigneproject":True,
        "enquirylist":enquirylist,
        "pm":pm,
    }
    return render (request,'pm/project/unassigneproject.html',context)         



@login_required(login_url='/')
@auth_pm
def addproject(request,id):
    pm = request.user.employee
    deatils= Enquiry.objects.get(id=id)
    form=ProjectForm(request.POST)
    if request.method == 'POST': 
        if form.is_valid():
            data = form.save()
            Project.objects.filter(id=data.id).update(enquiry=deatils)
            project = Project.objects.get(id=data.id)           
            Enquiry.objects.filter(id=id).update(status="Project Added")
            projectsrs=  SRS(project=project)
            projectsrs.save()

            return redirect('/pm/addteam/'+str(data.id))
        else:
            pass 
    else:

        context={
       
        "form":form,
        "pm":pm,
        }
        return render (request,'pm/project/addproject.html',context)
    return render (request,'pm/project/addproject.html',context)  



@login_required(login_url='/')
@auth_pm
def addteam(request,id):
    pm = request.user.employee
    employee = Employees.objects.filter(catagory__catagory__catagory_title="EMPLOYEE")
    context={
        "employee":employee,
        "id":id,
        "pm":pm,
    }
    return render (request,'pm/project/addteam.html',context)


@login_required(login_url='/')
@auth_pm
def client(request):

    form=ClientForm(request.POST) 
    clientdata =Client.objects.all()
    if request.method == 'POST': 
          
        if form.is_valid():           
            data = form.save() 
            form_data = Client.objects.get(id=data.id)
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,client=form_data)
            return redirect('pm:client')
        else:
            pass
    else:

        context = {
            "is_clientList":True,
            "form":form,
            "clientdata":clientdata
        }
        return render(request,'pm/client.html', context)






@login_required(login_url='/')
@auth_pm
def addschedule(request,id):
    pm = request.user.employee
    project_obj = Project.objects.get(id=id)
    team_mbr = ProjectMembers.objects.get(project=project_obj)
    mbr = ProjectMembers.objects.filter(project=project_obj)
    if request.method == 'POST':
        meetingDate = request.POST['meetingDate']
        platform = request.POST['platform']
        time = request.POST['time']
        link = request.POST['link']

        meeting = Meeting(project=project_obj,date=meetingDate,time=time,platform=platform,meeting_link=link)
        meeting.save()
        project_obj.status = "Waiting for SRS"
        project_obj.save()
        return redirect('pm:index')
        
    context = {
        "team":team_mbr,
        "mbr":mbr,
        "project":project_obj,
        "pm":pm,
        # "members":memberrs,
    }
    return render (request,'pm/project/addschedule.html',context)    



@login_required(login_url='/')
@auth_pm
def meetings(request):
    pm = request.user.employee  
    # meetings = Meeting.objects.filter(project__status="Meeting Scheduled")
    meetings = Meeting.objects.filter(project__status="Waiting for SRS")

    context = {
        "is_meetings":True,
        "meetings":meetings,
        "pm":pm,
    }
    return render(request,'pm/meetings.html',context)




@login_required(login_url='/')
@auth_pm
def task(request):
    pm = request.user.employee
    projects = Updation.objects.filter(status="CRM Checked")
    context = {
        "is_task":True,
        "projects" : projects,
        "pm":pm,
    }
    return render (request,'pm/project/task.html', context)


@csrf_exempt    
def taskmember(request):
    employeename=request.POST['employees']
    # leaderid=request.POST['leaderid']
    # employee_prjt = request.POST['memberObj']
    # projectid = request.POST['projectid']
    details=Employees.objects.get(name=employeename)
    print(details)
    member_prjct_obj = Task.objects.get(id=employee_prjt)
    member_prjct_obj.team.add(details)
    
    data={
        "id":details.id,
        "name":details.name,
        "catagory":details.catagory.title,
        "profile":details.emp_profile.url,

        
    }
    
   
    return JsonResponse({'value': data})


    

@login_required(login_url='/')
@auth_pm
def viewtask(request,id):
    print(id)
    updation=Updation.objects.get(id=id)
    if request.method =='POST':
        type = request.POST['type']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        print(type,startdate,enddate)
        taskobj = Task(project=updation, type=type, startdate=startdate, enddate=enddate)
        taskobj.save()
        id_only = str(taskobj.id)
        Updation.objects.filter(id=id).update(status="Team Assigned")
        return redirect('/pm/taskteam/'+ id_only)
        
     # employee = Employees.objects.filter(catagory__catagory__catagory_title="EMPLOYEE")
    # taskobj = Task(project=updation)
    # taskobj.save()
    context={
        "updation":updation,
        # "employee":employee
    }
    return render (request,'pm/project/viewtask.html',context)  


@login_required(login_url='/')
@auth_pm
def srs(request):
    pm = request.user.employee
    viewsrs = SRS.objects.filter(project__status='SRS uploaded')
    context={
        "is_srs":True,
        "viewsrs":viewsrs,
        "pm":pm,
    }
    return render (request,'pm/project/srs.html',context)  



@login_required(login_url='/')
@auth_pm
def fullprojectlist(request):
    pm = request.user.employee
    project = Project.objects.exclude(status="Completed")
    context = {
        "is_fullprojectlist":True,
        "pm":pm,
        "projects":project,
    }
    return render (request,'pm/project/fullprojectlist.html',context)  



@login_required(login_url='/')
@auth_pm
def dailyprogress(request):
    pm = request.user.employee
    today = datetime.now().date()
    # projectlists=DailyProgress.objects.filter(date=today).values('project__projectname','project__starteddate','project__endingdate','project__id').annotate(name_count=Count('project__projectname')).exclude(name_count=1)
    projectlists =DailyProgress.objects.filter(date=today).values('project__projectname','project__starteddate','project__endingdate','project__id').order_by('project').distinct()
    context={
        "is_dailyprogress":True,
        "projectlists":projectlists,
        "pm":pm,
    }
    return render (request,'pm/dailyprogress.html',context)    



@login_required(login_url='/')
@auth_pm
def viewdailyreport(request,id):
    pm = request.user.employee
    today = datetime.now().date()
    time = datetime.now().time()
    projectdata = Project.objects.get(id=id)
    morning= DailyProgress.objects.filter(date=today,project=projectdata,status='Morning')
    afternoon= DailyProgress.objects.filter(date=today,project=projectdata,status='Afternoon')
    evening= DailyProgress.objects.filter(date=today,project=projectdata,status='Evening')
    context={
        "morning":morning,
        "afternoon":afternoon,
        "evening":evening,
        "pm":pm,
    }
    return render (request,'pm/viewdailyreport.html',context)  
    


@login_required(login_url='/')
@auth_pm
def qcapprovel(request):
    pm = request.user.employee
    qclist= ProjectStatus.objects.filter(Q(status='Qc') & Q(completion__gte = 95))
    context ={
        "is_qcapprovel":True,
        "qclist":qclist ,
        "pm":pm,
    }
    return render (request,'pm/qcapprovel.html',context)   



@login_required(login_url='/')
@auth_pm
def leaverequest(request):
    pm = request.user.employee
    leave = LeaveRequests.objects.filter(pm_accept = False , status ='Waiting')
    context={
        "is_leaverequest":True,
        "leave":leave,
        "pm":pm,
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

    details=Employees.objects.get(name=employeename)
    member_obj = ProjectMembers(project=enqid,lead=details)
    member_obj.save()
    
    
    data={
        "id":details.id,
        "name":details.name,
        "member":member_obj.id,
        "profile":details.emp_profile.url,
       
        
    }
    
    
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
    
   
    return JsonResponse({'value': data})    




@csrf_exempt
def taskmembersearch(request):
    employeename=request.POST['member']
    taskid = request.POST['taskid']


     
    details=Employees.objects.get(name=employeename)
    member_prjct_obj = Task.objects.get(id=taskid)
    member_prjct_obj.team.add(details)
    # projectId = Project.objects.filter(id=projectid).update(status = "Team Ass")
    
    data={
        "id":details.id,
        "name":details.name,
        "catagory":details.catagory.title,

        
    }
    
   
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
def srsreject(request):
    id=request.POST['EnquaryID']
    Project.objects.filter(id=id).update(status = 'Waiting for SRS')
    return JsonResponse({'message': 'sucesses'}) 


@csrf_exempt
def Changedailyreport(request,id):
    DailyProgress.objects.filter(id=id).update(checked=True)
    return JsonResponse({'message': 'sucesses'}) 



@csrf_exempt
def changeqc(request):
    id=request.POST['id']
    ProjectStatus.objects.filter(id=id).update(status='W4C')
    return JsonResponse({'message': 'sucesses'}) 


@csrf_exempt
def rejectedqc(request,id):
    getdata=Project.objects.get(id=id)
    data ={
        'id':getdata.id,
    }
    return JsonResponse({'value':data})


@csrf_exempt
def qcrework(request):
    id=request.POST['id']
    typereason=request.POST['reason']
    projectidd=Project.objects.get(id=id)
    prostatus = ProjectStatus.objects.get(project=projectidd)
    reworkdata= Reworks(project=prostatus,note=typereason)
    reworkdata.save()
    projectcount = ProjectStatus.objects.get(project=projectidd)
    projectcount.rework_count = projectcount.rework_count + 1
    projectcount.save()
    status=ProjectStatus.objects.filter(project=projectidd).update(status='Rework',completion=94)
    return JsonResponse({'value': 'msg'})





@login_required(login_url='/')
def allstaff(request):
    all_emp = Employees.objects.all().order_by('name')

   
      
    context={
            "is_allstaff" : True,
            "employees":all_emp,
        }
    return render (request,'pm/allstaff.html',context)    




@login_required(login_url='/')
def departmentwise(request):
    department = SubCatagory.objects.all()
    class cat:
        def __init__(self,title,counts,id) :
            self.title = title
            self.counts = counts
            self.id = id

    estimatelist=[]
    for i in department:
        id=i.id
        emp_count = Employees.objects.filter(catagory=i).count()
       
        estimatelist.append(cat(i,emp_count,id))
      
    context = {
        "is_departmentwise" : True,
        "emp_count":estimatelist,
        # "departments":department,
            }
    return render (request,'pm/departmentwise.html',context)    




@login_required(login_url='/')
def employeelist(request,id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "category":category,
        "employees":employees
    }
    return render(request,'pm/employeelist.html',context)
 


@login_required(login_url='/')
def taskteam(request,id):
    print(id)
    employee = Employees.objects.filter(catagory__catagory__catagory_title="EMPLOYEE")
    context = {
        "employee":employee,
        "id":id,
    }
    return render(request,'pm/project/taskteam.html',context)

