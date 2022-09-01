from ast import And, Or
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import EmergenctContact, Employees, SubCatagory,TeamMembers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pm.models import ProjectMembers,Meeting ,Project,SRS,ProjectStatus,DailyProgress,ProjectProgressFiles
from gmanager.decorators import auth_employee

from django.db.models import Q
# Create your views here.


@login_required(login_url='/')
@auth_employee
def employeeHome(request):
    employeedata=Employees.objects.get(id=request.user.employee.id)
    listdata = ProjectStatus.objects.filter(member__team=employeedata) |ProjectStatus.objects.filter(member__lead=employeedata)
    
    context={
        "is_home":True,
        "employeedata":employeedata,
        "listdata":listdata,
    }
    return render(request,'employee/home.html',context)

@login_required(login_url='/')
@auth_employee
def viewproject(request):
  
    employeedata=Employees.objects.get(id=request.user.employee.id)
    meetinglist = ProjectMembers.objects.filter(team=employeedata ) | ProjectMembers.objects.filter(lead=employeedata)
    
    context = {
        "is_meeting":True,
        "meetinglist":meetinglist
    }
    return render(request,'employee/viewproject.html',context)



#------meeting ------
@login_required(login_url='/')
@auth_employee
def empMeetingLink(request,id):
    projectid= Project.objects.get(id=id)
    meetinglist = Meeting.objects.filter(project=projectid)
    if request.method == 'POST':
        fileuploads = request.FILES['fileupload']
        upoload=SRS(project=projectid,srsfile=fileuploads)
        upoload.save()
        Project.objects.filter(id=id).update(status='SRS uploaded')
        return redirect('/employee/viewproject')
    context = {
        "is_meeting":True,
        "meetinglist":meetinglist
      
    }
    return render(request,'employee/meeting_list.html',context)


# ----- Projects ------
@login_required(login_url='/')
@auth_employee
def allProjects(request):
    project_count = ProjectStatus.objects.filter(Q(member__lead = request.user.employee) | Q(member__team = request.user.employee)).count()
    print(project_count)
    ongoing = ProjectStatus.objects.filter(status = 'On Going').exclude(status='Qc')
    qc_projects = ProjectStatus.objects.filter(status='Qc')
    context = {
        "is_allprojects":True,
        "ongoing":ongoing,
        "qc_projects":qc_projects,
        "project_count":project_count
        
    }
    return render(request,'employee/projects.html',context)




@login_required(login_url='/')
@auth_employee
def empRework(request):
    context = {
        "is_rework":True,
    }
    return render(request,'employee/rework.html',context)


@login_required(login_url='/')
@auth_employee
def empDailyProgress(request,id):
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
       
        ProjectStatus.objects.filter(project=project_obj).update(status=projectstatus, completion=percentage, url_project=link, username=username, password=password)
        valuesss=DailyProgress(project=project_obj,employee=employee_id,status=timetype,note=instruction)
        valuesss.save()
       

        return redirect('/employee')
    context = {
        "is_dailyprogress":True,
        "proj_sts":proj_sts,
       
    }
    return render(request,'employee/daily_progress.html',context)


@login_required(login_url='/')
@auth_employee
def empProgressReport(request,id):
    projectdetails= Project.objects.get(id=id)
    projectstatus = ProjectStatus.objects.get(project=projectdetails)
    members =ProjectMembers.objects.filter(project=projectdetails).values('team__name','team__id')
    daily_report = DailyProgress.objects.filter(project=projectdetails).values('date','status','note','employee__name')
   
   
    context = {
        "is_progressreport":True,
        "projectdetails":projectdetails,
        "projectstatus":projectstatus,
        "members":members,
        # "totalReport":totalReport,
        "daily_report":daily_report,

    }
    return render(request,'employee/progress_report.html',context)

@login_required(login_url='/')
@auth_employee
def empTask(request):
    context = {
        "is_task":True,
    }
    return render(request,'employee/task.html',context)

@login_required(login_url='/')
@auth_employee
def empHomework(request):
    context = {
        "is_homework":True,
    }
    return render(request,'employee/homework.html',context)


# ------ Leaves ------
@login_required(login_url='/')
@auth_employee
def leaveApplication(request):
    context = {
        "is_attendance":True,
    }
    return render(request,'employee/leave_application.html',context)

@login_required(login_url='/')
@auth_employee
def empAttendance(request):
    context = {
        "is_attendance":True,
    }
    return render(request,'employee/attendance.html',context)



# ----- employee ------
@login_required(login_url='/')
def allEmployees(request):
    all_emp = Employees.objects.all().order_by('name')
    context = {
        "is_employee":True,
        "all_emp" :all_emp,
    }
    return render(request,'employee/all_employees.html',context)


@login_required(login_url='/')
@auth_employee
def empDepartment(request):
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
        # "departments":department,
            }
    return render(request,'employee/department.html',context)


def departmentwiseEmployee(request,id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "category":category,
        "employees":employees
    }
    return render(request,'employee/departmentwise_employee.html',context)



@login_required(login_url='/')
@auth_employee
def empTimeline(request):
    employee_timeline = Employees.objects.all().order_by('-join_date')
    context = {
        "is_timeline":True,
        "employee_timeline":employee_timeline
    }
    return render(request,'employee/timeline.html',context)



# ------ team -------
@login_required(login_url='/')
@auth_employee
def empTeam(request):
    emp= Employees.objects.get(id=request.user.employee.id)
    team_name = TeamMembers.objects.get(employee=emp)
    ream_all = TeamMembers.objects.filter(teamname=team_name.teamname)
    print(ream_all)
    context = {
        "is_team":True,
        "team_name":ream_all,
    }
    return render(request,'employee/team.html',context)


#------ Profile ------
@login_required(login_url='/')
@auth_employee
def empProfile(request):
    emp=EmergenctContact.objects.get(employee=request.user.employee)
    context = {
        "is_profile":True,
        "emp":emp,
    }
    return render(request,'employee/profile.html',context)





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