
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import EmergenctContact, Employees, SubCatagory, TeamMembers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from pm.models import ProjectMembers, Meeting ,Project,SRS,ProjectStatus,DailyProgress,ProjectProgressFiles, Reworks, Task, Updation
from gmanager.decorators import auth_employee
import datetime
from django.db.models import Q
from datetime import datetime
from pytz import timezone 
# from django.contrib.auth import logout
# Create your views here.







def base(request):
    print('hello')
    return render(request,'employee/base.html')
# ----- home -----
@login_required(login_url='/')
@auth_employee
def employeeHome(request):
    emp = request.user.employee
    print(emp)
    employeedata=Employees.objects.get(id=request.user.employee.id)
    listdata = ProjectStatus.objects.filter(member__team=employeedata ).exclude(status='Completed') |ProjectStatus.objects.filter(member__lead=employeedata).exclude(status='Completed')
    member = ProjectStatus.objects.filter(member__team=employeedata).count()
    lead =ProjectStatus.objects.filter(member__lead=employeedata).count()

    



    meetinglist1 = ProjectMembers.objects.filter(team=employeedata,project__status='Waiting for SRS' ).count()
    meetinglist2 =  ProjectMembers.objects.filter(lead=employeedata,project__status='Waiting for SRS').count()
    meetingcount =meetinglist1 + meetinglist2
    print(meetingcount)
    reworklist1 = Reworks.objects.filter(project__member__team=employeedata,status='Not Seen').count()
    reworklist2= Reworks.objects.filter(project__member__lead=employeedata,status='Not Seen').count()
    reworkcount=reworklist1 + reworklist2
    # listdatasss = ProjectStatus.objects.get(member__team=employeedata,status='Rework')
    # reworklist = Reworks.objects.filter(project=listdatasss,status='Not Seen').count()
    # print(reworklist)
    # |ProjectStatus.objects.filter(member__lead=employeedata).count()
    context={
        "is_home":True,
        "employeedata":employeedata,
        "listdata":listdata,
        "emp":emp,
        "lead":lead,
        "member":member,
        "meetingcount":meetingcount,
        "reworkcount":reworkcount
    }
    return render(request,'employee/home.html',context)



# -----projects -------
@login_required(login_url='/')
@auth_employee
def viewproject(request):
    emp = request.user.employee
    employeedata=Employees.objects.get(id=request.user.employee.id)
    meetinglist = ProjectMembers.objects.filter(team=employeedata,project__status='Waiting for SRS' ) | ProjectMembers.objects.filter(lead=employeedata,project__status='Waiting for SRS')
    
    context = {
        "is_meeting":True,
        "meetinglist":meetinglist,
        "emp":emp
    }
    return render(request,'employee/viewproject.html',context)



#------meeting ------
@login_required(login_url='/')
@auth_employee
def empMeetingLink(request,id):
    emp = request.user.employee
    projectid= Project.objects.get(id=id)
    meetinglist = Meeting.objects.filter(project=projectid)
    # today = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%d-%m')
    # print(today)
    todate = datetime.now()

    print(todate.date(),'%'*29)
    to_date = todate.date().strftime('%Y-%m-%d')
    # print(to_date,"%"*10)
    if request.method == 'POST':
        fileuploads = request.FILES['fileupload']
        print(fileuploads,'88'*10)
        
        
        # upoload=SRS.objects.filter(project=projectid).update(srsfile=fileuploads)
        # print(upoload,'scucess'*2)
        # Project.objects.filter(id=id).update(status='SRS uploaded')
        # return redirect('/employee/viewproject')
        upoload=SRS.objects.get(project=projectid)
        upoload.srsfile = fileuploads
        upoload.save()
        print(upoload,'scucess'*2)
        Project.objects.filter(id=id).update(status='SRS uploaded')
        return redirect('/employee/viewproject')
    context = {
        "emp":emp,
        "is_meeting":True,
        "meetinglist":meetinglist,
        "projectid":projectid
      
    }
    return render(request,'employee/meeting_list.html',context)



# ----- Projects list------
@login_required(login_url='/')
@auth_employee
def allProjects(request):
    emp = request.user.employee
    project_count = ProjectStatus.objects.filter(Q(member__lead = request.user.employee) | Q(member__team = request.user.employee)).count()
    print(project_count)
    ongoing = ProjectStatus.objects.filter(status = 'On Going').exclude(status='Qc')
    qc_projects = ProjectStatus.objects.filter(status = 'Qc')
    allproject =ProjectStatus.objects.filter(Q(member__lead = request.user.employee) | Q(member__team = request.user.employee))
    projectlist= ProjectStatus.objects.all()
    context = {
        "emp":emp,
        "is_allprojects":True,
        "ongoing":ongoing,
        "qc_projects":qc_projects,
        "project_count":project_count,
        "allproject":allproject,
        "projectlist":projectlist
        
    }
    return render(request,'employee/projects.html',context)



# ---- rework----
@login_required(login_url='/')
@auth_employee
def empRework(request):
    emp = request.user.employee
    employeedata=Employees.objects.get(id=request.user.employee.id)
    
    reworklist = Reworks.objects.filter(project__member__team=employeedata,status='Not Seen') | Reworks.objects.filter(project__member__lead=employeedata,status='Not Seen')
 
    context = {
        "is_rework":True,
        "emp":emp,
        "reworklist":reworklist
        }
    return render(request,'employee/rework.html',context)
    # if ProjectStatus.objects.filter(member__team=employeedata,status='Rework').exists():
    #     listdata = ProjectStatus.objects.get(member__team=employeedata,status='Rework')
    #     reworklist = Reworks.objects.filter(project=listdata,status='Not Seen')
    #     context = {
    #     "is_rework":True,
    #     "emp":emp,
    #     "reworklist":reworklist
    #     }
    #     return render(request,'employee/rework.html',context)
    # else:
    #     return render(request,'employee/rework.html')

    # |ProjectStatus.objects.filter(member__lead=employeedata)
    # reworklist = Reworks.objects.filter(project=listdata,status='Not Seen')
    # print(reworklist)
    # context = {
    #     "is_rework":True,
    #     "emp":emp,
    #     "reworklist":reworklist
    # }
    # return render(request,'employee/rework.html',context)



# ------ daily progress -------
@login_required(login_url='/')
@auth_employee
def empDailyProgress(request,id):
    emp = request.user.employee
    print(request.user.employee.catagory.title)
    project_obj = Project.objects.get(id=id)
    proj_sts = ProjectStatus.objects.get(project=project_obj)
    employee_id = Employees.objects.get(id=request.user.employee.id)
    if request.method =='POST':
        projectstatus = request.POST['projectstatus']
        percentage = request.POST['percentage']
        timetype = request.POST['timetype']
        link = request.POST['link']
        username = request.POST['username']
        password = request.POST['password']
        instruction = request.POST['instruction']
        # fileupload = ""
        fileupload =request.FILES.get('fileupload', "New default that isn't None")
        print(fileupload,"%"*10)

        if fileupload != None:
            print("if worked","7"*10)

            ProjectStatus.objects.filter(project=project_obj).update(status=projectstatus, completion=percentage, url_project=link, username=username, password=password)
            valuesss=DailyProgress(project=project_obj,employee=employee_id,status=timetype,note=instruction)
            valuesss.save()
            uploded= ProjectProgressFiles(project=project_obj,files=fileupload)
            uploded.save()
            return redirect('/employee')
        else:
            print("else worked","0"*10)
            ProjectStatus.objects.filter(project=project_obj).update(status=projectstatus, completion=percentage, url_project=link, username=username, password=password)
            valuesss=DailyProgress(project=project_obj,employee=employee_id,status=timetype,note=instruction)
            valuesss.save()   
            return redirect('/employee')

       

    context = {
        "is_dailyprogress":True,
        "proj_sts":proj_sts,
        "emp":emp,
       
    }
    return render(request,'employee/daily_progress.html',context)


#  ----- daily progress report ------
@login_required(login_url='/')
@auth_employee
def empProgressReport(request,id):
    emp = request.user.employee
    projectdetails= Project.objects.get(id=id)
    projectstatus = ProjectStatus.objects.get(project=projectdetails)
    members =ProjectMembers.objects.filter(project=projectdetails).values('team__name','team__id')
    daily_report = DailyProgress.objects.filter(project=projectdetails).values('date','status','note','employee__name')
    
    context = {
        "emp":emp,
        "is_progressreport":True,
        "projectdetails":projectdetails,
        "projectstatus":projectstatus,
        "members":members,
        # "totalReport":totalReport,
        "daily_report":daily_report,

    }
    return render(request,'employee/progress_report.html',context)



# ----- task -----
@login_required(login_url='/')
@auth_employee
def empTask(request):
    emp = request.user.employee

    employeedata=Employees.objects.get(id=request.user.employee.id)
    taskdetails = Task.objects.filter(team=employeedata )
    print(taskdetails)
    context = {
        "is_task":True,
        "emp":emp,
        "taskdetails":taskdetails
    }
    return render(request,'employee/task.html',context)


# -----homework-------
@login_required(login_url='/')
@auth_employee
def empHomework(request):
    emp = request.user.employee
    context = {
        "is_homework":True,
        "emp":emp
    }
    return render(request,'employee/homework.html',context)


# ------ Leaves ------
@login_required(login_url='/')
@auth_employee
def leaveApplication(request):
    emp = request.user.employee
    context = {
        "is_attendance":True,
        "emp":emp
    }
    return render(request,'employee/leave_application.html',context)


# -----attendance------
@login_required(login_url='/')
@auth_employee
def empAttendance(request):
    emp = request.user.employee
    context = {
        "is_attendance":True,
        "emp":emp
    }
    return render(request,'employee/attendance.html',context)



# ----- allemployee ------
@login_required(login_url='/')
def allEmployees(request):
    emp = request.user.employee
    all_emp = Employees.objects.all().order_by('name')
    context = {
        "is_employee":True,
        "all_emp" :all_emp,
        "emp":emp
    }
    return render(request,'employee/all_employees.html',context)


# -----department-------
@login_required(login_url='/')
@auth_employee
def empDepartment(request):
    emp = request.user.employee
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
        "is_department":True,
        "emp_count":estimatelist,
        "emp":emp
        # "departments":department,
    }
    return render(request,'employee/department.html',context)


# ------- departmentwise employee------
def departmentwiseEmployee(request,id):
    emp = request.user.employee
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "emp":emp,
        "category":category,
        "employees":employees
    }
    return render(request,'employee/departmentwise_employee.html',context)


# ----timeline------
@login_required(login_url='/')
@auth_employee
def empTimeline(request):
    emp = request.user.employee
    employee_timeline = Employees.objects.all().order_by('-join_date')
    context = {
        "emp":emp,
        "is_timeline":True,
        "employee_timeline":employee_timeline
    }
    return render(request,'employee/timeline.html',context)



# ------ team -------
@login_required(login_url='/')
@auth_employee
def empTeam(request):
    emp = request.user.employee
    emp= Employees.objects.get(id=request.user.employee.id)
    if TeamMembers.objects.filter(employee=emp).exists():

        team_name = TeamMembers.objects.get(employee=emp)
        ream_all = TeamMembers.objects.filter(teamname=team_name.teamname)
        # employee_details = ProjectStatus.objects.all()
        # print(employee_details)
        context = {
            "is_team":True,
            "emp":emp,
            "team_name":ream_all,
            # "employee_details":employee_details
        }
        return render(request,'employee/team.html',context)
    else:
        context = {
            "is_team":True,
            "emp":emp,
            # "employee_details":employee_details
        }
        return render(request,'employee/team.html',context)



#------ Profile ------
@login_required(login_url='/')
@auth_employee
def empProfile(request):
    emp = request.user.employee
    employee=EmergenctContact.objects.get(employee=request.user.employee)
    context = {
        "is_profile":True,
        "emp":emp,
        "employee":employee,
    }
    return render(request,'employee/profile.html',context)


# -----profiledata-----
@csrf_exempt
def getprofiledata(request,id):
    details=Employees.objects.get(id=id)
    data={
        "name":details.name,
        "catagory":details.catagory.title,
        "employee_id":details.employee_id,
        "email":details.email,
        "dob":details.dob,
        "address":details.address,
       "emp_profile":details.emp_profile.url,

    }
    return JsonResponse({'value': data})


def getdata(request,id):
    details = Employees.objects.get(id=id)
    # project = ProjectMembers.objects.get(team=details)
    data={
        "name":details.name,
        "catagory":details.catagory.title,
        "employee_id":details.employee_id,
        "email":details.email,
        "dob":details.dob,
        "address":details.address,
       "emp_profile":details.emp_profile.url,
    #    "project_name":project.project.projectname,
    #    "client":project.project.client,
    #    "startdate":project.project.client.starteddate,
    #    "enddate":project.project.client.endingdate,
    }
    return JsonResponse({'value': data})




@csrf_exempt
def Reworkstatus(request):
    id=request.POST['EnquaryID']
    Reworks.objects.filter(id=id).update(status = 'Seen')
    return JsonResponse({'message': 'sucesses'}) 


def projeclist(request):
    
    return render(request,'employee/projeclist.html')



def detailview(request,id):
    emp = request.user.employee
    projectdetail = Project.objects.get(id=id)
    daily_report = DailyProgress.objects.filter(project=projectdetail).values('date','status','note','employee__name')
    progressreport = ProjectStatus.objects.get(project=projectdetail)
    members =ProjectMembers.objects.filter(project=projectdetail)
    viewsrs =SRS.objects.get(project=projectdetail)
    uploadedfiles = ProjectProgressFiles.objects.filter(project=projectdetail).exclude(files="New default that isn't None")
    # print(uploadedfiles,'$$'*34)
    

    context={
        "emp":emp,
        "projectdetail":projectdetail,
        "daily_report":daily_report,
        "progressreport":progressreport,
        "members":members,
        "viewsrs":viewsrs,
        "uploadedfiles":uploadedfiles
    }
    return render(request,'employee/detailviewproject.html',context)


# def logout_view(request):
#     logout(request)
#     return redirect('ceo:login')    


def countval(request):
    

    employeedata=Employees.objects.get(id=request.user.employee.id)
    meetinglist1 = ProjectMembers.objects.filter(team=employeedata,project__status='Waiting for SRS' ).count()
    meetinglist2= ProjectMembers.objects.filter(lead=employeedata,project__status='Waiting for SRS').count()
    meetingcount = int(meetinglist1)+int(meetinglist2)
    return meetingcount



@csrf_exempt
def taskdetails(request,id):
    getdata =  Updation.objects.get(id=id)
    data ={
        'note':getdata.note,
        'date':getdata.date,
        'files':getdata.files.url,    
    }
    # print(data.files)
    return JsonResponse({'value': data})    

def taskreport(request,id):
    return render(request,'employee/taskreport.html')
