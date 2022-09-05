
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from ceo.models import Client
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pm.models import Project,SRS,ProjectStatus,Updation,Reworks
# Create your views here.
@login_required(login_url='/')
def base(request):
    return render (request,'clients/partials/base.html')


@login_required(login_url='/')
def home(request):
    name= request.user.client.name
  
    clientid =Client.objects.get(id=request.user.client.id)
   
    project =Project.objects.filter(client=clientid)
    print(project)

    context={
        "project":project
    }
    return render (request,'clients/home.html',context)




@login_required(login_url='/')
def viewproject(request,id):
   
   
    project =Project.objects.get(id=id)
    viewsrs= SRS.objects.filter(project=project)
    projectdetails =ProjectStatus.objects.filter(project=project)

    context ={
        "viewsrs":viewsrs,
        "projectdetails":projectdetails,
        "project":project.id
        

    }
    return render (request,'clients/viewproject.html',context)




# @login_required(login_url='/')
# def home(request):
#     name= request.user.client.name
  
#     clientid =Client.objects.get(id=request.user.client.id)
   
#     project =Project.objects.get(client=clientid)
#     viewsrs= SRS.objects.filter(project=project)
#     projectdetails =ProjectStatus.objects.filter(project=project)

#     context ={
#         "viewsrs":viewsrs,
#         "projectdetails":projectdetails,
#         "project":project.id
        

#     }
#     return render (request,'clients/index.html',context)    





@login_required(login_url='/')
def updation(request):
    if request.method == 'POST':
        updation = request.POST['updation']
        projectid = request.POST['projectid']
        
        upload = request.FILES['upload']
        project_id =Project.objects.get(id=projectid)
        update = Updation(project=project_id,note=updation, files=upload)
        update.save()
        return redirect('/clients')



@login_required(login_url='/')
def payment(request):
    return render (request,'clients/payment.html')    



@csrf_exempt
def completedproject(request):
    id=request.POST['id']
    ProjectStatus.objects.filter(id=id).update(status = 'Completed',completion=100)
    return JsonResponse({'message': 'sucesses'})     



@csrf_exempt
def Getid(request,id):
    getdata=Project.objects.get(id=id)
    data ={
        'id':getdata.id,
    }
    return JsonResponse({'value':data})    



@csrf_exempt
def clientrework(request):
    id=request.POST['id']
    typereason=request.POST['reason']
    projectidd=Project.objects.get(id=id)
    prostatus = ProjectStatus.objects.get(project=projectidd)
    reworkdata= Reworks(project=prostatus,note=typereason)
    reworkdata.save()
    status=ProjectStatus.objects.filter(project=projectidd).update(status='Rework',completion=96)
    return JsonResponse({'value': 'msg'})
