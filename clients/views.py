
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from ceo.models import Client

from pm.models import Project,SRS,ProjectStatus,Updation
# Create your views here.
@login_required(login_url='/')
def base(request):
    return render (request,'clients/partials/base.html')

@login_required(login_url='/')
def home(request):
    
    clientid =Client.objects.get(id=request.user.client.id)
   
    project =Project.objects.get(client=clientid)
    viewsrs= SRS.objects.filter(project=project)
    projectdetails =ProjectStatus.objects.filter(project=project)

    context ={
        "viewsrs":viewsrs,
        "projectdetails":projectdetails,
        "project":project.id
        

    }
    return render (request,'clients/index.html',context)    


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