from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class EnquiryNote(models.Model):
    description = HTMLField()
    added_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default="Active")

    def __str__(self):
        return str(self.added_time)


class Enquiry(models.Model):
    choices = (
        ("Web Services", "Web Services"),
        ("Mobile Application", "Mobile Application"),
        ("Seo", "Seo"),
        ("Graphic Designing", "Graphic Designing"),
        ("Digital Marketing", "Digital Marketing"),
    )
    Enquirynote = models.ForeignKey(EnquiryNote, on_delete=models.CASCADE, null=True)
    enquirydate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default="Enquiry")
    projectname = models.CharField(max_length=50, null=True)
    companyname = models.CharField(max_length=50, null=True)
    clientname = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(default=0, null=True, max_length=15)
    whatsapp = models.CharField(default=0, null=True, max_length=15)
    referredby = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True, choices=choices)
    files = models.FileField(
        upload_to="Enquiry/", max_length=100000, blank=True, null=True
    )
    details = models.CharField(max_length=1000000, null=True)
    reason = models.CharField(max_length=1000000, null=True, default="no reason")
    address = models.CharField(max_length=1000000, null=True, blank=True)

    def __str__(self):
        return str(self.projectname)
