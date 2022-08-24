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