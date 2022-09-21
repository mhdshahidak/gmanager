from django import forms
from ceo.models import EmergenctContact, Employees
from .models import *
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput,PasswordInput,DateInput
 



class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model = Employees
        exclude = ('status', '')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Name','name':'name'}),
            'employee_id': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'employee_id','name':'employee_id'}),
            'catagory' : Select(attrs={'class': 'form-control bx-inp', 'required': 'required','name':'catagory','name':'catagory'}),
            'email': EmailInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off', 'placeholder':'E-mail','name':'email'}),
            'phone': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Phone','name':'phone'}),
            'dob': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'dob','name':'dob','type':'date'}),
            'whatsapp_number': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'whatsapp_number','name':'whatsapp_number'}),
            'join_date': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'join_date','name':'join_date','type':'date'}),
            'address': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'address','name':'address'}),
            'district': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'District','name':'district'}),
            'state': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'State','name':'state'}),
            'nationality': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Nationality','name':'nationality'}),
            'marital_status': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Marital status','name':'marital_status'}),
            'emp_profile' : FileInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off','name':'emp_profile','id':'emp_profile'}),
            'username': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'username','name':'username','id':'checkusername'}),
            'password': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            # 'c_password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'c_password','name':'c_password'}),
            
        }


class EmergenctContactForm(forms.ModelForm):
    class Meta:
        model = EmergenctContact
        fields = ('primarycontact_name', 'emergency_number', 'relation')
        widgets = {
            'primarycontact_name': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Name','name':'primarycontact_name'}),
            'emergency_number':TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'emergency_number','name':'emergency_number'}),
            'relation' : TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Name','name':'relation'}),
        }