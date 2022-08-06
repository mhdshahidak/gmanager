from django.shortcuts import render

# Create your views here.

def crmHome(request):
    context = {
        "is_home":True,
    }
    return render(request,'crm/home.html',context)


def enquiryList(request):
    context = {
        "is_enquiryList":True,
    }
    return render(request,'crm/enquirylist.html', context)


def clientList(request):
    context = {
        "is_clientList":True,
    }
    return render(request,'crm/clientlist.html', context)


def projectList(request):
    context = {
        "is_projectList":True,
    }
    return render(request,'crm/projectlist.html', context)


def followUpList(request):
    context = {
        "is_followUpList":True,
    }
    return render(request,'crm/followuplist.html', context)


def feedBack(request):
    context = {
        "is_feedBack":True,
    }
    return render(request,'crm/feedback.html', context)


def leaves(request):
    context = {
        "is_leaves":True,
    }
    return render(request,'crm/leaves.html', context)


def attantance(request):
    context = {
        "is_attantance":True,
    }
    return render(request,'crm/attantance.html', context)


def settings(request):
    context = {
        "is_settings":True,
    }
    return render(request,'crm/settings.html', context)


def profile(request):
    context = {
        "is_profile":True,
    }
    return render(request,'crm/profile.html', context)