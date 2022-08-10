from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def employeeHome(request):
    context={
        "is_home":True,
    }
    return render(request,'employee/home.html',context)


#------meeting ------
def empMeetingLink(request):
    context = {
        "is_meeting":True,
    }
    return render(request,'employee/meeting_list.html',context)


# ----- Projects ------
def allProjects(request):
    context = {
        "is_allprojects":True,
    }
    return render(request,'employee/projects.html',context)

def projectSrs(request):
    context = {
        "is_srs":True,
    }
    return render(request,'employee/srs.html',context)

def empRework(request):
    context = {
        "is_rework":True,
    }
    return render(request,'employee/rework.html',context)


def empDailyProgress(request):
    context = {
        "is_dailyprogress":True,
    }
    return render(request,'employee/daily_progress.html',context)

def empProgressReport(request):
    context = {
        "is_progressreport":True,
    }
    return render(request,'employee/progress_report.html',context)

def empTask(request):
    context = {
        "is_task":True,
    }
    return render(request,'employee/task.html',context)

def empHomework(request):
    context = {
        "is_homework":True,
    }
    return render(request,'employee/homework.html',context)

# ------ Leaves ------
def empAttendance(request):
    context = {
        "is_attendance":True,
    }
    return render(request,'employee/attendance.html',context)



# ----- employee ------
def allEmployees(request):
    context = {
        "is_employee":True,
    }
    return render(request,'employee/all_employees.html',context)

def empDepartment(request):
    context = {
        "is_department":True,
    }
    return render(request,'employee/department.html',context)

def empTimeline(request):
    context = {
        "is_timeline":True,
    }
    return render(request,'employee/timeline.html',context)

# ------ team -------
def empTeam(request):
    context = {
        "is_team":True,
    }
    return render(request,'employee/team.html',context)


#------ Profile ------
def empProfile(request):
    context = {
        "is_profile":True,
    }
    return render(request,'employee/profile.html',context)