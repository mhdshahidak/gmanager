from django.shortcuts import render

# Create your views here.

def leave_application(request):
    return render(request,'common/leave_apply.html')


def attendanceRreport(request):
    return render(request,'common/attendance_report.html')


def settings(request):
    return render(request,'common/settings.html')