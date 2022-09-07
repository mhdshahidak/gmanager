from django.shortcuts import render,redirect
from . form import EnquiryForm,ClientForm
from . models import *
from ceo.models import Client, EmergenctContact, Employees,Attendence,SubCatagory
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from pm.models import Updation ,Project
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
from gmanager.decorators import auth_crm

# Create your views here.


@login_required(login_url='/')
@auth_crm
def crmHome(request):

    crm_rrr = request.user.employee.catagory.title

    todate = today = datetime.datetime.now()

    enquirylist = EnquiryNote.objects.filter(status = 'Active').count()
    enquirylistToday = EnquiryNote.objects.filter(status = 'Active',added_time__gte=todate).count()
    addedtoprop = Enquiry.objects.filter(status = 'Added To Proposal').count()
    billcreation = Enquiry.objects.filter(status = 'Bill Creation').count()
    billadvance = Enquiry.objects.filter(status = 'Bill Advance').count()
    advancepaid = Enquiry.objects.filter(status = 'Advance Paid').count()
    rejected = Enquiry.objects.filter(status = 'Rejected').count()
    clientsCount = Client.objects.all().count()
    clients = Client.objects.all()
    projectcount = Project.objects.all().count()
    completed_project = Project.objects.filter(status="Completed").count()

    if request.method == 'POST':        
        instructions = request.POST['instruction']

        new_project_note = EnquiryNote(description=instructions)
        new_project_note.save()       
        return redirect('crm:crmhome')
                
    context = {
        "is_home":True,
        "projectcount":projectcount,
        "completed":completed_project,
        "addedtoprop":addedtoprop,
        "billcreation":billcreation,
        "billadvance":billadvance,
        "advancepaid":advancepaid,
        "rejected":rejected,
        "enquirylist":enquirylist,
        "enquirylistToday":enquirylistToday,
        "clientsCount":clientsCount,
        "clients":clients,
        
    }
    return render(request,'crm/home.html',context)

@login_required(login_url='/')
@auth_crm
def enquiryList(request):
    enquirylistdata = EnquiryNote.objects.filter(status='Active')
    context = {
        "is_enquiryList":True,
        "enquirylistdata":enquirylistdata
    }
    return render(request,'crm/enquirylist.html', context)

@login_required(login_url='/')
@auth_crm
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
@auth_crm
def projectList(request):
    enquiry  = Enquiry.objects.all()
    context =  {
        "is_projectList":True,
        "enquiry":enquiry,
    }
    return render(request,'crm/projectlist.html', context)

@login_required(login_url='/')
@auth_crm
def followUpList(request):
    updationlist = Updation.objects.filter(status='Not Checked')
    context = {
        "is_followUpList":True,
        "updationlist":updationlist
    }
    return render(request,'crm/followuplist.html', context)

@login_required(login_url='/')
@auth_crm
def feedBack(request):
    context = {
        "is_feedBack":True,
    }
    return render(request,'crm/feedback.html', context)

@login_required(login_url='/')
@auth_crm
def leaves(request):
    context = {
        "is_leaves":True,
    }
    return render(request,'crm/leaves.html', context)

@login_required(login_url='/')
@auth_crm
def attantance(request):
    context = {
        "is_attantance":True,
    }
    return render(request,'crm/attantance.html', context)

@login_required(login_url='/')
@auth_crm
def settings(request):
    context = {
        "is_settings":True,
    }
    return render(request,'crm/settings.html', context)

@login_required(login_url='/')
@auth_crm
def profile(request):
    context = {
        "is_profile":True,
    }
    return render(request,'crm/profile.html', context)

@login_required(login_url='/')
@auth_crm
def viewenquiry(request,id):
    details = EnquiryNote.objects.get(id=id)
   
    context = {
        "details":details,
        "id":id
    }
    return render(request,'crm/viewenquiry.html',context)


@login_required(login_url='/')
@auth_crm
def createProject(request,id):
    details = EnquiryNote.objects.get(id=id)
    form=EnquiryForm(request.POST,request.FILES)
    if request.method == 'POST': 
      
        if form.is_valid():
            data = form.save()           
            Enquiry.objects.filter(id=data.id).update(Enquirynote=details) 
            EnquiryNote.objects.filter(id=id).update(status='DeActivate')   
            return redirect('/crm/addclient')
            
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




@login_required(login_url='/')
@auth_crm
def attantanceList(request):
    allemp = Employees.objects.all()
    if request.method =='POST':
        attendence = request.POST.getlist('attendence[]')
        date = request.POST['date']
        punchin = request.POST['punchin']
        punchout = request.POST['punchout']
        Employeeid = request.POST['Employeeid']
        employdata =Employees.objects.get(id=Employeeid)
        saveattendence= Attendence(employee=employdata, date=date ,punch_intime=punchin, punch_outtime=punchout)
        saveattendence.save()
        if len(attendence) == 1 :
            for i in enumerate(attendence):
                if i[1]=='Morning':
                    Attendence.objects.filter(id=saveattendence.id).update(morning=True)
                    return redirect ('/crm/attantancelist')

                elif i[1] == 'Afternoon':
                    Attendence.objects.filter(id=saveattendence.id).update(evening=True)
                    return redirect ('/crm/attantancelist')   

                else:
                    print('dfvsfvbgf','@'*10)
        elif len(attendence) == 2 :
            Attendence.objects.filter(id=saveattendence.id).update(morning=True,evening=True)
            return redirect ('/crm/attantancelist')
        else :
            return redirect ('/crm/attantancelist')

    context = {
        "is_attantanceList":True,
        "allemp" : allemp,
    }
    return render(request, 'crm/attantancelist.html',context)



def leave(request):
    if request.method =='POST':
        date = request.POST['date']
        Employeeid = request.POST['idleave']
        employdata =Employees.objects.get(id=Employeeid)
        saveattendence= Attendence(employee=employdata, date=date, status='Leave')
        saveattendence.save()
        return redirect ('/crm/attantancelist')




@csrf_exempt
def getemployeedata(request,id):
    details =Employees.objects.get(id=id)

    data={
        "id":details.id,
        "name":details.name,
        "employeeid":details.employee_id,
         "catagory":details.catagory.title,
        
    }
    return JsonResponse({'value': data})


@csrf_exempt
def getemployeeleave(request,id):
    details =Employees.objects.get(id=id)

    data={
        "id":details.id,
        "name":details.name,
        "employeeid":details.employee_id,
         "catagory":details.catagory.title,
        
    }
    return JsonResponse({'value': data})


@login_required(login_url='/')
@auth_crm
def attantanceReport(request):
    if request.method =='POST':
        serachdate = request.POST['serachdate']
        serachdate = request.POST['serachdate']
        if Attendence.objects.filter(date=serachdate).exists():
            presentdate = Attendence.objects.filter(status='Present').count()
            absentdate = Attendence.objects.filter(status='Leave').count()
            employeedetails = Attendence.objects.filter(date=serachdate).all()

            context={
                "is_attantanceReport":True,
                "presentdate":presentdate,
                "absentdate":absentdate,
                "employeedetails":employeedetails,
                 "status":0

            }
            return render(request, 'crm/attantancereport.html',context)


        else:
            context={
                "status":1
            }
            return render(request, 'crm/attantancereport.html',context)
    context = {
        "is_attantanceReport":True,
    }
    return render(request, 'crm/attantancereport.html',context)




@login_required(login_url='/')
def allstaff(request):
    all_emp = Employees.objects.all().order_by('name')

   
      
    context={
            "is_allstaff" : True,
            "employees":all_emp,
        }
    return render (request,'crm/allstaff.html',context)    




@login_required(login_url='/')
def departmentwise(request):
    department = SubCatagory.objects.all()
    class cat:
        def __init__(self,title,counts,id) :
            self.title = title
            self.counts = counts
            self.id = id

    estimatelist=[]
    for i in department:
        id=i.id
        emp_count = Employees.objects.filter(catagory=i).count()
       
        estimatelist.append(cat(i,emp_count,id))
      
    context = {
        "is_departmentwise" : True,
        "emp_count":estimatelist,
        # "departments":department,
            }
    return render (request,'crm/departmentwise.html',context)    




@login_required(login_url='/')
def employeelist(request,id):
    category = SubCatagory.objects.get(id=id)
    employees = Employees.objects.filter(catagory=category)
    context = {
        "category":category,
        "employees":employees
    }
    return render(request,'crm/employeelist.html',context)
 




def addclient(request):
    form=ClientForm(request.POST) 
    clientdata =Client.objects.all()
    if request.method == 'POST': 
          
        if form.is_valid():           
            data = form.save() 
            form_data = Client.objects.get(id=data.id)
            User = get_user_model()
            User.objects.create_user(username=form_data.username, password=form_data.password,client=form_data)
            return redirect('/crm/clientlist')
        else:
            pass
    else:

        context = {
            "is_clientList":True,
            "form":form,
            "clientdata":clientdata
        }
    return render(request,'crm/addclient.html',context)