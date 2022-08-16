from django.shortcuts import render,redirect

from ceo.models import *
from django.contrib.auth import get_user_model
from . forms import LeaveRequestsForm

# Create your views here.

def leave_application(request):
    user_name = request.user.employee
    leave_form = LeaveRequestsForm(request.POST or None)
    # now_date = datetime.now()
    if request.method == "POST":
        if leave_form.is_valid():           
                data = leave_form.save()            
                LeaveRequests.objects.filter(id=data.id).update(employee=user_name)                             
                return redirect('common:leaveapplication')
        else:
            pass
    # print(user_name)
    context = {
        'user':user_name,
        'leaveform':leave_form,
    }
    return render(request,'common/leave_apply.html', context)


def attendanceRreport(request):
    return render(request,'common/attendance_report.html')


def settings(request):
    return render(request,'common/settings.html')