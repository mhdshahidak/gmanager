from django.db import models

from crm.models import Enquiry

from ceo.models import Employees,Client

# Create your models here.





class Praposalpdf(models.Model):
    enquiry= models.ForeignKey(Enquiry, on_delete = models.CASCADE,null=True)
    praposalpdf = models.FileField(upload_to="Praposalpdf/", max_length=100000)

    def __str__(self):
        return str(self.enquiry)        


class Project(models.Model):
    choices = (('Low','Low'),('Medium','Medium'),('High','High'))
    enquiry = models.ForeignKey(Enquiry, on_delete = models.CASCADE,null=True)
    client = models.ForeignKey(Client, on_delete = models.CASCADE,null=True)
    status = models.CharField(max_length = 25,default= 'Schedule Meeting')
    projectname = models.CharField(max_length = 50,null=True)
    starteddate = models.DateTimeField()
    endingdate = models.DateTimeField()
    projecttype = models.CharField(max_length = 50,null=True, choices=choices)





class ProjectMembers (models.Model):  
    project = models.ForeignKey(Project, on_delete = models.CASCADE,null=True)  
    lead = models.ForeignKey(Employees, on_delete = models.CASCADE,null=True, related_name='lead')
    team = models.ManyToManyField(Employees,related_name='team')



class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField()
    platform = models.CharField(max_length=50,null=True)
    meeting_link = models.CharField(max_length=2000,null=True)
            

class SRS(models.Model): 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    srsfile = models.FileField(upload_to="Praposalpdf/", max_length=100000)
    added_time = models.DateTimeField(auto_now_add=True)



class ProjectStatus(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  
    member = models.ForeignKey(ProjectMembers, on_delete = models.CASCADE,null=True) 
    status = models.CharField(max_length=30, null=True, default="Not Started")
    completion = models.IntegerField(default=0)
    url_project = models.URLField(max_length=1000, null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)


class ProjectProgressFiles(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    files = models.FileField(null=True)



class DailyProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete = models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, default="Add Note")
    status = models.CharField(max_length=15, default="Not Checked")
    checked = models.BooleanField(default=False)





class Updation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField(null=True, default="Add Note")
    date = models.DateTimeField(auto_now_add=True)
    files = models.FileField(null=True,default='default_img.jpg')
    status = models.CharField(max_length=15, default="Not Checked")


