
from django.shortcuts import render,redirect
from . form import EnquiryForm,ClientForm

from . models import *
from ceo.models import Client, EmergenctContact, Employees,Attendence,SubCatagory
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from pm.models import Praposalpdf, Updation ,Project,ProjectStatus,ProjectMembers,Meeting,SRS,DailyProgress
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
# from datetime import date
from gmanager.decorators import auth_crm
from pm.form import PraposalpdfForm,ProjectForm
# Create your views here.


@login_required(login_url='/')
@auth_crm
def crmHome(request):

    crm_rrr = request.user.employee.catagory.title

    # todate = datetime.datetime.now().date() 
    enquirylist = EnquiryNote.objects.filter(status = 'Active').count()
    # enquirylistToday = EnquiryNote.objects.filter(status = 'Active',added_time__date=todate).count()
    # print(enquirylistToday)
    addedtoprop = Enquiry.objects.filter(status = 'Added To Proposal').count()
    billcreation = Enquiry.objects.filter(status = 'Bill Creation').count()
    billadvance = Enquiry.objects.filter(status = 'Bill Advance').count()
    advancepaid = Enquiry.objects.filter(status = 'Advance Paid',type='Graphic Designing').count()
    # enquirylist = Enquiry.objects.filter(status = 'Advance Paid',type='Graphic Designing')
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
        # "enquirylistToday":enquirylistToday,
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
def graphicenquiry(request):
    enquirylistdata = Enquiry.objects.filter(status = 'Enquiry',type='Graphic Designing')
    print(enquirylistdata)
    context ={
        "enquirylistdata":enquirylistdata,
    }
    return render(request,'crm/graphicenquiry.html', context)



@login_required(login_url='/')
@auth_crm
def viewgraphicenquries(request,id):
    details = Enquiry.objects.get(id=id)
    if request.method == 'POST': 
        pro=Praposalpdf(enquiry=details,praposalpdf="no")
        pro.save()
        Enquiry.objects.filter(id=id).update(status = 'Bill Creation')
        return redirect('/crm/')

    else:
        context={
        "details":details ,
    }
    return render (request,'crm/viewgraphicenquries.html',context) 

    # forms=PraposalpdfForm(request.POST,request.FILES)
    # if request.method == 'POST': 
    #     if forms.is_valid():
    #         data = forms.save()
    #         data.enquiry=details
    #         data.save()
    #         Enquiry.objects.filter(id=id).update(status = 'Added To Proposal')
    #         return redirect('/crm/')
    #     else:
    #         pass 
    # else:

    #     context={
    #     "details":details ,
    #     "forms":forms,
      
    #     }
    #     return render (request,'crm/viewgraphicenquries.htmll',context) 
    # context={
    #     "details":details ,
    # }
    # return render (request,'crm/viewgraphicenquries.html',context) 



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
    form2=ClientForm(request.POST) 
    if request.method == 'POST': 
      
        if form.is_valid():
            data = form.save()           
            Enquiry.objects.filter(id=data.id).update(Enquirynote=details) 
            EnquiryNote.objects.filter(id=id).update(status='DeActivate')  
            if data.type =="Graphic Designing":
                print("if")
                Enquiry.objects.filter(id=data.id).update(status="Added To Proposal")
                return redirect('/crm/')
            else:
                print("else")
                pass 
                return redirect('/crm/')               
            return redirect('/crm/')
            
    context = {
        "details":details,
        "form":form,
        "form2":form2,
        "id":id
    }
    
    return render(request,'crm/create_project.html',context)
    

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




@csrf_exempt
def viewdata(request,id):
    details=Updation.objects.get(id=id)
    
    data={
        "note":details.note,
        "date":details.date.date(),
        "file":details.files.url,
       
        

    }
    return JsonResponse({'value': data})    

@csrf_exempt
def changedata(request,id):
    Updation.objects.filter(id=id).update(status='CRM Checked')
    
    return JsonResponse({'value': 'data'})  



@login_required(login_url='/')
@auth_crm
def proposal(request):
    data = Enquiry.objects.filter(status = 'Added To Proposal')
   
    context ={
        "is_proposal":True,
        "data":data,
       
    }
    return render(request,'crm/parposal.html',context)


@csrf_exempt
def savaProposal(request):
    id=request.POST['EnquaryID']
    Enquiry.objects.filter(id=id).update(status = 'Bill Creation')
    # if Enquiry__type==""
    prop=Enquiry.objects.get(id=id)
    if prop.type=="Graphic Designing":
        print(prop.type)
        getenq= Enquiry.objects.get(id=id)
        prpr=Praposalpdf(enquiry=getenq)
        prpr.save()
        return JsonResponse({'message': 'sucesses'})
    else:
        return JsonResponse({'message': 'sucesses'})    

    
    # return JsonResponse({'message': 'sucesses'}) 

@csrf_exempt
def rejectedreason(request,id):
    details=Enquiry.objects.get(id=id)
    
    data={
        "id":details.id,
    }
    return JsonResponse({'value': data})

@csrf_exempt
def typereason(request):
    id=request.POST['id']
    typereason=request.POST['reason']
    Enquiry.objects.filter(id=id).update(status='Rejected',reason=typereason)
    return JsonResponse({'value': 'msg'})


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
        # serachdate = request.POST['serachdate']
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
 






def deleteenquery(request,id):
    EnquiryNote.objects.get(id=id).delete()
    return redirect('/crm/enquirylist')


def editclient(request,id):
    clientdetails= Client.objects.get(id=id)
    if request.method =='POST':
        name = request.POST['name']
        companyname = request.POST['companyname']
        phone = request.POST['phone']
        Whatsapp = request.POST['Whatsapp']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']
        Client.objects.filter(id=id).update(name=name, companyname=companyname, address=address, phone=phone, email=email, whatsapp_number=Whatsapp, username=username, password=password)
        print(username,password,'$'*38)
        password_upadte = get_user_model().objects.get(client=clientdetails)
        password_upadte.set_password(password)
        password_upadte.save()
        get_user_model().objects.filter(client=clientdetails).update(username=username)
        return redirect('/crm/clientlist')
    else:

        context={
            "clientdetails":clientdetails,
        }
        return render(request,'crm/editclient.html',context)
    



def deleteclient(request,id):
    Client.objects.get(id=id).delete()
    return redirect('/crm/clientlist')

@login_required(login_url='/')
@auth_crm
def unassigneproject(request):
    enquirylist = Enquiry.objects.filter(status = 'Advance Paid',type='Graphic Designing')
    context={
        "is_unassigneproject":True,
        "enquirylist":enquirylist,
    }
    return render (request,'crm/unassigneproject.html',context)         


@login_required(login_url='/')
@auth_crm
def meetinglist(request):
    meetinglist = Meeting.objects.filter(project__enquiry__type = "Graphic Designing",project__status="Waiting for SRS")
   
    context={
        "is_meetinglist":True,
        "meetinglist":meetinglist,
    }
    return render (request,'crm/meetinglist.html',context) 



@login_required(login_url='/')
@auth_crm
def addproject(request,id):
    pm = request.user.employee
    deatils= Enquiry.objects.get(id=id)
    form=ProjectForm(request.POST)
    if request.method == 'POST': 
        if form.is_valid():
            data = form.save()
            Project.objects.filter(id=data.id).update(enquiry=deatils)
            project = Project.objects.get(id=data.id)           
            Enquiry.objects.filter(id=id).update(status="Project Added")
            projectsrs=  SRS(project=project)
            projectsrs.save()

            return redirect('/crm/addteam/'+str(data.id))
        else:
            pass 
    else:

        context={
       
        "form":form,
        "pm":pm,
        }
        return render (request,'crm/addproject.html',context)
    return render (request,'crm/addproject.html',context)  



@login_required(login_url='/')
@auth_crm
def addteam(request,id):
    employee = Employees.objects.filter(catagory__catagory__catagory_title="EMPLOYEE")
    context={
        "employee":employee,
        "id":id,
    }
    return render (request,'crm/addteam.html',context)


@login_required(login_url='/')
@auth_crm
def addschedule(request,id):
    project_obj = Project.objects.get(id=id)
    team_mbr = ProjectMembers.objects.get(project=project_obj)
    mbr = ProjectMembers.objects.filter(project=project_obj)
    if request.method == 'POST':
        meetingDate = request.POST['meetingDate']
        platform = request.POST['platform']
        time = request.POST['time']
        link = request.POST['link']

        meeting = Meeting(project=project_obj,date=meetingDate,time=time,platform=platform,meeting_link=link)
        meeting.save()
        project_obj.status = "Waiting for SRS"
        project_obj.save()
        return redirect('crm:crmhome')
        
    context = {
        "team":team_mbr,
        "mbr":mbr,
        "project":project_obj,
        # "members":memberrs,
    }
    return render (request,'crm/addschedule.html',context)      


@csrf_exempt
def meetingapproved(request):
    id=request.POST['EnquaryID']
    print(id,'&'*29)
    Project.objects.filter(id=id).update(status = 'SRS Approved')
    
    proj = Project.objects.get(id=id)
    member = ProjectMembers.objects.get(project=proj)

    new_projectstatus = ProjectStatus(project=proj,member=member)
    new_projectstatus.save()
    addedprogres = DailyProgress(project=proj)
    addedprogres.save()
    
    return JsonResponse({'message': 'sucesses'}) 





@login_required(login_url='/')
@auth_crm
def dailyprogress(request):
    today = datetime.now().date()
    # projectlists=DailyProgress.objects.filter(date=today).values('project__projectname','project__starteddate','project__endingdate','project__id').annotate(name_count=Count('project__projectname')).exclude(name_count=1)
    projectlists =DailyProgress.objects.filter(date=today,project__enquiry__type="Graphic Designing").values('project__projectname','project__starteddate','project__endingdate','project__id').order_by('project').distinct()
    context={
        "is_dailyprogress":True,
        "projectlists":projectlists,
    }
    return render (request,'crm/dailyprogress.html',context)     



@login_required(login_url='/')
@auth_crm
def viewdailyreport(request,id):
    today = datetime.now().date()
    time = datetime.now().time()
    projectdata = Project.objects.get(id=id)
    morning= DailyProgress.objects.filter(date=today,project=projectdata,status='Morning')
    afternoon= DailyProgress.objects.filter(date=today,project=projectdata,status='Afternoon')
    evening= DailyProgress.objects.filter(date=today,project=projectdata,status='Evening')
    context={
        "morning":morning,
        "afternoon":afternoon,
        "evening":evening,
    }
    return render (request,'crm/viewdailyreport.html',context) 


@csrf_exempt
def Changedailyreport(request,id):
    DailyProgress.objects.filter(id=id).update(checked=True)
    return JsonResponse({'message': 'sucesses'}) 
