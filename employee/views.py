from django.shortcuts import render

# Create your views here.

def employeeHome(request):
    return render(request,'employee/home.html')


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