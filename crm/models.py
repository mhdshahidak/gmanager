from django.db import models
from tinymce.models import HTMLField
import datetime
from phone_field import PhoneField
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.


class EnquiryNote(models.Model):
    description = HTMLField()
    added_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 25,default= 'Active')
    def __str__(self):
        return str(self.added_time)




class Enquiry(models.Model):
    choices = (('Web Services','Web Services'),('Mobile','Mobile'),('Seo','Seo'),('Graphics','Graphics'))
    Enquirynote = models.ForeignKey(EnquiryNote, on_delete = models.CASCADE,null=True)
    enquirydate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 25,default= 'Enquiry')
    projectname = models.CharField(max_length = 50,null=True)
    companyname = models.CharField(max_length = 50,null=True)
    clientname = models.CharField(max_length = 50,null=True)
    email = models.EmailField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    whatsapp = PhoneField(blank=True, help_text='Whatsapp number')
    referredby = models.CharField(max_length = 50,null=True)
    type = models.CharField(max_length = 50,null=True, choices=choices)
    files = models.FileField(upload_to="Enquiry/", max_length=100000)
    details = models.CharField(max_length = 1000000,null=True)
    reason = models.CharField(max_length = 1000000,null=True,default= 'no reason')


    def __str__(self):
        return str(self.projectname)        