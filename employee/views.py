from ast import And, Or
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ceo.models import EmergenctContact, Employees
from pm.models import ProjectMembers,Meeting ,Project,SRS
# Create your views here.


@login_required(login_url='/')
def employeeHome(request):
    context={
        "is_home":True,
    }
    return render(request,'employee/home.html',context)

@login_required(login_url='/')
def viewproject(request):
    print(request.user.id)
    # meetinglist = ProjectMembers.objects.filter(team=request.user.id)
    employeedata=Employees.objects.get(id=request.user.employee.id)
    print(employeedata)
    meetinglist=ProjectMembers.objects.filter(team=employeedata ) | ProjectMembers.objects.filter(lead=employeedata)
    
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
def empDailyProgress(request):
    context = {
        "is_dailyprogress":True,
    }
    return render(request,'employee/daily_progress.html',context)


@login_required(login_url='/')
def empProgressReport(request):
    context = {
        "is_progressreport":True,
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

