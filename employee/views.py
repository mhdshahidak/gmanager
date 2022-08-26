from ast import And, Or
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import EmergenctContact, Employees
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pm.models import ProjectMembers,Meeting ,Project,SRS,ProjectStatus,DailyProgress,ProjectProgressFiles
# Create your views here.


@login_required(login_url='/')
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
def viewproject(request):
    print(request.user.id)
    # meetinglist = ProjectMembers.objects.filter(team=request.user.id)
    employeedata=Employees.objects.get(id=request.user.employee.id)
    print(employeedata)
    meetinglist = ProjectMembers.objects.filter(team=employeedata ) | ProjectMembers.objects.filter(lead=employeedata)
    
    print(meetinglist)
    context = {
        "is_meeting":True,
        "meetinglist":meetinglist
    }
    return render(request,'employee/viewproject.html',context)



#------meeting ------
@login_required(login_url='/')
def empMeetingLink(request,id):
    print(id)
    projectid= Project.objects.get(id=id)
    meetinglist = Meeting.objects.filter(project=projectid)
    print(meetinglist)
    if request.method == 'POST':
        fileuploads = request.FILES['fileupload']
        print(fileuploads)
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
def allProjects(request):
    context = {
        "is_allprojects":True,
    }
    return render(request,'employee/projects.html',context)


# @login_required(login_url='/')
# def projectSrs(request):
#     employeedata=Employees.objects.get(id=request.user.employee.id)
#     print(employeedata)
#     meetinglist=ProjectMembers.objects.filter(team=employeedata ) | ProjectMembers.objects.filter(lead=employeedata)
#     context = {
#         "is_srs":True,
#         "meetinglist":meetinglist
#     }
#     return render(request,'employee/srs.html',context)


@login_required(login_url='/')
def empRework(request):
    context = {
        "is_rework":True,
    }
    return render(request,'employee/rework.html',context)


@login_required(login_url='/')
def empDailyProgress(request,id):
    # print(request.user.employee.id,'$'*99)
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
def empProgressReport(request,id):
    projectdetails= Project.objects.get(id=id)
    projectstatus = ProjectStatus.objects.get(project=projectdetails)
    members =ProjectMembers.objects.filter(project=projectdetails).values('team__name','team__id')
    # totalReport = DailyProgressTotal.objects.get(project=projectdetails)
    daily_report = DailyProgress.objects.filter(project=projectdetails).values('date','status','note','employee__name')
    # daily_report = DailyProgress.objects.filter(project=projectdetails).values('date','status','note')
    print(daily_report)
   
   
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
def empTask(request):
    context = {
        "is_task":True,
    }
    return render(request,'employee/task.html',context)

@login_required(login_url='/')
def empHomework(request):
    context = {
        "is_homework":True,
    }
    return render(request,'employee/homework.html',context)


# ------ Leaves ------
@login_required(login_url='/')
def leaveApplication(request):
    context = {
        "is_attendance":True,
    }
    return render(request,'employee/leave_application.html',context)

@login_required(login_url='/')
def empAttendance(request):
    context = {
        "is_attendance":True,
    }
    return render(request,'employee/attendance.html',context)



# ----- employee ------
@login_required(login_url='/')
def allEmployees(request):
    context = {
        "is_employee":True,
    }
    return render(request,'employee/all_employees.html',context)

@login_required(login_url='/')
def empDepartment(request):
    context = {
        "is_department":True,
    }
    return render(request,'employee/department.html',context)

@login_required(login_url='/')
def empTimeline(request):
    context = {
        "is_timeline":True,
    }
    return render(request,'employee/timeline.html',context)

# ------ team -------
@login_required(login_url='/')
def empTeam(request):
    context = {
        "is_team":True,
    }
    return render(request,'employee/team.html',context)


#------ Profile ------
@login_required(login_url='/')
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

    }
    return JsonResponse({'value': data})