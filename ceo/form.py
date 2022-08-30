from django import forms
from .models import *
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput,PasswordInput,DateInput
 



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('name','employee_id','email','phone','whatsapp_number','catagory','username','password','address','dob','join_date')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Name','name':'name'}),
            'employee_id': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'employee_id','name':'employee_id'}),
            'email': EmailInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off', 'placeholder':'E-mail','name':'email'}),
            'phone': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Phone','name':'phone'}),
            'whatsapp_number': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'whatsapp_number','name':'whatsapp_number'}),
            # 'files' : FileInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off','name':'file','id':'files'}),
            'catagory' : Select(attrs={'class': 'form-control bx-inp', 'required': 'required','name':'catagory','name':'catagory'}),
            'username': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'username','name':'username'}),
            'password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            # 'c_password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'c_password','name':'c_password'}),
            'address': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'address','name':'address'}),
            'dob': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'dob','name':'dob','type':'date'}),
            'join_date': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'join_date','name':'join_date','type':'date'}),

        }


class editEmployeeForm(forms.ModelForm):
      class Meta:
        model = Employees
        fields = ('name','employee_id','email','phone','whatsapp_number','catagory','username','password','address','dob','join_date')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Name','name':'name'}),
            'employee_id': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'employee_id','name':'employee_id'}),
            'email': EmailInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off', 'placeholder':'E-mail','name':'email'}),
            'phone': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Phone','name':'phone'}),
            'whatsapp_number': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'whatsapp_number','name':'whatsapp_number'}),
            # 'files' : FileInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off','name':'file','id':'files'}),
            'catagory' : Select(attrs={'class': 'form-control bx-inp', 'required': 'required','name':'catagory','name':'catagory'}),
            # 'username': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'username','name':'username'}),
            # 'password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            # 'c_password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'c_password','name':'c_password'}),
            'address': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'address','name':'address'}),
            'dob': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'dob','name':'dob','type':'date'}),
            'join_date': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'join_date','name':'join_date','type':'date'}),

        }