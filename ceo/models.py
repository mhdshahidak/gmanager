from django.db import models
from phone_field import PhoneField
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



class Catagoty(models.Model):
    catagoty_title = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.catagoty_title)


class SubCatagory(models.Model):
    catagoty = models.ForeignKey(Catagoty, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)

    def __str__(self):
        return str(self.title)




class Employees(models.Model):
    name = models.CharField(max_length = 200)
    employee_id = models.CharField(max_length = 25)
    catagoty = models.ForeignKey(SubCatagory, on_delete = models.PROTECT)
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
    emp_profile = VersatileImageField(upload_to = 'empProfile',ppoi_field='image_ppoi',blank =True, null = True)
    image_ppoi = PPOIField()
    status = models.CharField(max_length = 25,default= 'Online')
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.name)


class EmergenctContact(models.Model):
    emergency_number = PhoneField(blank=True, help_text='Contact phone number')
    primarycontact_name = models.CharField(max_length = 25, null = True)
    relation = models.CharField(max_length = 25, null = True)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.primarycontact_name)




class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    email=models.EmailField(unique=True)
    username = models.CharField(max_length = 50, unique=True)
    phone_number=PhoneField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='username'



