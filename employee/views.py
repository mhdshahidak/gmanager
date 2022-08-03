from django.shortcuts import render

# Create your views here.

def employeeHome(request):
    return render(request,'employee/home.html')


# ----- Projects ------
def allProjects(request):
    return render(request,'employee/projects.html')

def empDailyProgress(request):
    return render(request,'employee/daily_progress.html')

def empProgressReport(request):
    return render(request,'employee/progress_report.html')

def empTask(request):
    return render(request,'employee/task.html')

def empHomework(request):
    return render(request,'employee/homework.html')



# ----- employee ------
def allEmployees(request):
    return render(request,'employee/all_employees.html')

def empDepartment(request):
    return render(request,'employee/department.html')

def empTimeline(request):
    return render(request,'employee/timeline.html')
# ------ team -------

def empTeam(request):
    return render(request,'employee/team.html')


#------ Profile ------
def empProfile(request):
    return render(request,'employee/profile.html')