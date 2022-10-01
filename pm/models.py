from django.db import models

from ceo.models import Client, Employees
from crm.models import Enquiry

# Create your models here.


class Praposalpdf(models.Model):
    enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE, null=True)
    praposalpdf = models.FileField(upload_to="Praposalpdf/", max_length=100000)

    def __str__(self):
        return str(self.enquiry)


class Project(models.Model):
    choices = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))
    enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=25, default="Schedule Meeting")
    projectname = models.CharField(max_length=50, null=True)
    starteddate = models.DateTimeField()
    endingdate = models.DateTimeField()
    projecttype = models.CharField(max_length=50, null=True, choices=choices)

    def get_members(self):
        return ProjectMembers.objects.filter(project=self)

    def get_progres(self):
        return ProjectStatus.objects.filter(project=self)


class ProjectMembers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    lead = models.ForeignKey(
        Employees, on_delete=models.CASCADE, null=True, related_name="lead"
    )
    team = models.ManyToManyField(Employees, related_name="team")


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField()
    platform = models.CharField(max_length=50, null=True)
    meeting_link = models.CharField(max_length=2000, null=True)


class SRS(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    srsfile = models.FileField(null=True, default="deafult-01.jpg", upload_to="srs/")


class ProjectStatus(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(ProjectMembers, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=30, null=True, default="Not Started")
    completion = models.IntegerField(default=0)
    url_project = models.URLField(max_length=1000, null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    rework_count = models.IntegerField(default=0)


class ProjectProgressFiles(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    files = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class DailyProgress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    note = models.TextField(null=True, default="Add Note")
    status = models.CharField(max_length=15, default="Not Checked")
    checked = models.BooleanField(default=False)


class Updation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField(null=True, default="Add Note")
    date = models.DateTimeField(auto_now_add=True)
    files = models.FileField(
        null=True, default="default_img.jpg", blank=True, upload_to="Updation/"
    )
    status = models.CharField(max_length=15, default="Not Checked")


class Reworks(models.Model):
    project = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    note = models.TextField(null=True, default="Add Note")
    status = models.CharField(null=True, max_length=15, default="Not Seen")


class Task(models.Model):
    project = models.ForeignKey(Updation, on_delete=models.CASCADE)
    team = models.ManyToManyField(Employees, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=15, null=True, blank=True)
