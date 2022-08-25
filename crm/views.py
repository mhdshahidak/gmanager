from django.shortcuts import render,redirect
from . form import EnquiryForm,ClientForm
from . models import *
from ceo.models import Client, EmergenctContact, Employees
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from pm.models import Updation ,Project
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.



def crmHome(request):
    # emp = Employees.objects.get(id=request.user.employee.id)
    # emp1 = emp.id
    # form=EnquirynoteForm(request.POST)  
    # print(emp1)  
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
            # "emp1":emp1
            
        }
    else: 
        print('#'*10)         
        context = {
            "is_home":True,
            
        }
        return render(request,'crm/home.html',context)
    return render(request,'crm/home.html',context)

@login_required(login_url='/')
def enquiryList(request):
    enquirylistdata = EnquiryNote.objects.filter(status='Active')
    context = {
        "is_enquiryList":True,
        "enquirylistdata":enquirylistdata
    }
    return render(request,'crm/enquirylist.html', context)

@login_required(login_url='/')
def clientList(request):
    form=ClientForm(request.POST) 
    clientdata =Client.objects.all()
    if request.method == 'POST': 
          
        if form.is_valid():           
            data = form.save() 
            form_data = Client.objects.get(id=data.id)
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,client=form_data)
            return redirect('crm:clientlist')
        else:
            pass
    else:

        context = {
            "is_clientList":True,
            "form":form,
            "clientdata":clientdata
        }
        return render(request,'crm/clientlist.html', context)

@login_required(login_url='/')
def projectList(request):
    context = {
        "is_projectList":True,
    }
    return render(request,'crm/projectlist.html', context)

@login_required(login_url='/')
def followUpList(request):
    updationlist = Updation.objects.filter(status='Not Checked')
    context = {
        "is_followUpList":True,
        "updationlist":updationlist
    }
    return render(request,'crm/followuplist.html', context)

@login_required(login_url='/')
def feedBack(request):
    context = {
        "is_feedBack":True,
    }
    return render(request,'crm/feedback.html', context)

@login_required(login_url='/')
def leaves(request):
    context = {
        "is_leaves":True,
    }
    return render(request,'crm/leaves.html', context)

@login_required(login_url='/')
def attantance(request):
    context = {
        "is_attantance":True,
    }
    return render(request,'crm/attantance.html', context)

@login_required(login_url='/')
def settings(request):
    context = {
        "is_settings":True,
    }
    return render(request,'crm/settings.html', context)

@login_required(login_url='/')
def profile(request):
    context = {
        "is_profile":True,
    }
    return render(request,'crm/profile.html', context)

@login_required(login_url='/')
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


@login_required(login_url='/')
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
    






@csrf_exempt
def viewdata(request,id):
    details=Updation.objects.get(id=id)
    
    data={
        "note":details.note,
        "date":details.date,
       
        

    }
    return JsonResponse({'value': data})    

@csrf_exempt
def changedata(request,id):
    Updation.objects.filter(id=id).update(status='CRM Checked')
    
    return JsonResponse({'value': 'data'})  

    