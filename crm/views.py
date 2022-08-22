from django.shortcuts import render,redirect
from . form import EnquiryForm
from . models import *

# Create your views here.

def crmHome(request):
    # form=EnquirynoteForm(request.POST)  
    # print(form)  
    # print (form.errors)
    if request.method == 'POST': 
        # print (form.errors) 
        # print('*'*10)      
        # if form.is_valid():           
        #     form.save()

        #     return redirect('crm:enquirylist')
        # else:
        #     pass
        print("success")
        instructions = request.POST['instruction']
        # exam = Exam.objects.get(id=id)
        print(instructions)

        new_project_note = EnquiryNote(description=instructions)
        new_project_note.save()
        context = {
            "is_home":True,
            
        }
    else: 
        print('#'*10)         
        context = {
            "is_home":True,
            
        }
        return render(request,'crm/home.html',context)
    return render(request,'crm/home.html',context)


def enquiryList(request):
    enquirylistdata = EnquiryNote.objects.filter(status='Active')
    context = {
        "is_enquiryList":True,
        "enquirylistdata":enquirylistdata
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

def viewenquiry(request,id):
    details = EnquiryNote.objects.get(id=id)
    # form=EnquiryForm(request.POST,request.FILES)  
    # if request.method == 'POST': 
    #     # print (form.errors) 
    #     if form.is_valid():
    #         print (form.errors) 
    #         data = form.save()            
    #         Enquiry.objects.filter(id=data.id).update(Enquirynote=details) 
    #         EnquiryNote.objects.filter(id=id).update(status='DeActivate')   
    #         return redirect('crm:crmhome')
    #     else:
    #         pass
    context = {
        "details":details,
        "id":id
    }
    return render(request,'crm/viewenquiry.html',context)


def createProject(request,id):
    details = EnquiryNote.objects.get(id=id)
    form=EnquiryForm(request.POST,request.FILES)
    if request.method == 'POST': 
        # print (form.errors)
        print("Test"*5) 
        if form.is_valid():
            data = form.save()
            print("*"*20)           
            Enquiry.objects.filter(id=data.id).update(Enquirynote=details) 
            EnquiryNote.objects.filter(id=id).update(status='DeActivate')   
            return redirect('crm:crmhome')
        else:
            pass
    context = {
        "details":details,
        "form":form,
        "id":id
    }
    
    return render(request,'crm/create_project.html',context)
    