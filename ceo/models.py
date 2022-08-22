from django.db import models
from phone_field import PhoneField
import datetime
from versatileimagefield.fields import VersatileImageField, PPOIField

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):

        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user
    def create_superuser(self,username,password=None,**extra_fields):

        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff   = True
        user.save(using=self._db)
        return user



class Catagory(models.Model):
    catagory_title = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.catagory_title)


class SubCatagory(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)

    def __str__(self):
        return str(self.title)




class Employees(models.Model):
    name = models.CharField(max_length = 200)
    employee_id = models.CharField(max_length = 25)
    catagory = models.ForeignKey(SubCatagory, on_delete = models.PROTECT)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField()
    dob = models.DateField(null = True)
    whatsapp_number = PhoneField(blank=True, help_text='Contact phone number')
    join_date = models.DateField()
    address = models.CharField(max_length = 200, null = True)
    district = models.CharField(max_length = 25, null = True)
    state = models.CharField(max_length = 25, null = True)
    nationality = models.CharField(max_length = 30, null = True)
    marital_status = models.CharField(max_length = 10, null = True)
    emp_profile = VersatileImageField(upload_to = 'empProfile', null = True)
    status = models.CharField(max_length = 25,default= 'Online')
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.name)


class EmergenctContact(models.Model):
    emergency_number = PhoneField(blank=True, help_text='Contact phone number')
    primarycontact_name = models.CharField(max_length = 25, null = True)
    relation = models.CharField(max_length = 25, null = True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.primarycontact_name)




class User(AbstractBaseUser, PermissionsMixin):  
    username = models.CharField(max_length = 50, unique=True)
    phone_number=PhoneField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='username'





class LeaveRequests(models.Model):
    leave_choices = (('Casual Leave','Casual Leave'),('Sick Leave','Sick Leave'),('Maternity Leave','Maternity Leave'),('Compensatory Off','Compensatory Off'),('Marriage Leave','Marriage Leave'),('Other','Other'))
    employee  = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    leave_type = models.CharField(max_length=30, choices=leave_choices)
    aply_date = models.DateField(auto_now_add=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    no_days = models.IntegerField(default=0,null=True)
    reason = models.CharField(max_length=1000,null=True)
    hr_accept = models.BooleanField(default=False)
    pm_accept = models.BooleanField(default=False)
    status = models.CharField(max_length = 25,default= 'Waiting')
    rejected_reason = models.CharField(max_length=1000,null=True)



class ExcuseRequests(models.Model):
    employee  = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    aply_date = models.DateField(auto_now_add=True)
    from_date = models.DateField(null=True)
    time = models.TimeField(null=True)
    reason = models.CharField(max_length=1000,null=True)
    status = models.CharField(max_length = 25,default= 'Waiting')
