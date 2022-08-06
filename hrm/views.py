from django.shortcuts import render

# Create your views here.

def hrmHome(request):
    context = {
        "is_hrmHome":True,
    }
    return render(request, 'hrm/hrmhome.html',context)


def employeeList(request):
    context = {
        "is_employeeList":True,
    }
    return render(request, 'hrm/employees.html',context)



def clientList(request):
    context = {
        "is_clientList":True,
    }
    return render(request, 'hrm/client.html',context)


def leaveRequest(request):
    context = {
        "is_leaveRequest":True,
    }
    return render(request, 'hrm/leaverequest.html',context)


def leaveReport(request):
    context = {
        "is_leaveReport":True,
    }
    return render(request, 'hrm/leavereport.html',context)


def attantanceReport(request):
    context = {
        "is_attantanceReport":True,
    }
    return render(request, 'hrm/attantancereport.html',context)


def hrsettings(request):
    context = {
        "is_hrsettings":True,
    }
    return render(request, 'hrm/hrsettings.html',context)


def attantanceList(request):
    context = {
        "is_attantanceList":True,
    }
    return render(request, 'hrm/attantancelist.html',context)
