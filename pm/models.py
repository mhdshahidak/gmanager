from django.db import models

from crm.models import Enquiry
# Create your models here.





class Praposalpdf(models.Model):
    enquiry= models.ForeignKey(Enquiry, on_delete = models.CASCADE,null=True)
    praposalpdf = models.FileField(upload_to="Praposalpdf/", max_length=100000)

    def __str__(self):
        return str(self.enquiry)        