from ceo.models import *
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput,PasswordInput,DateInput,TimeInput
 

class LeaveRequestsForm(forms.ModelForm):
    class Meta:
        model = LeaveRequests
        fields = ('leave_type','from_date','to_date','no_days','reason')
        widgets = {
            'leave_type': Select(attrs={'class': 'form-control','required': 'required', 'autocomplete':'off', 'placeholder':'Leave Type','name':'name'}),
            'from_date': DateInput(attrs={'class': 'form-control','required': 'required', 'autocomplete':'off', 'placeholder':'From Date','name':'fromdate','type':'date'}),
            'to_date': DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'To Date','name':'todate','type':'date'}),
            'no_days': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'No of Days','name':'no-of-days'}),
            'reason': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'reason','name':'reason'}),           
           
        }



class ExcuseRequestsForm(forms.ModelForm):
    class Meta:
        model = ExcuseRequests
        fields = ('from_date','time','reason')
        widgets = {
            'from_date': DateInput(attrs={'class': 'form-control','required': 'required', 'autocomplete':'off', 'placeholder':'From Date','name':'fromdate','type':'date'}),
            'time': TimeInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Time','name':'time','type':'time'}),
            'reason': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'reason','name':'reason'}),           
           
        }


class ProfileResetForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('name', 'employee_id','email','phone','whatsapp_number','emp_profile','catagory','username','password','address','dob','join_date','district','state','nationality','marital_status')
        Widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'name'}),
            'employee_id':forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'employee_id'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'email'}),
            'phone': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'phone'}),
            'whatsapp_number': forms.NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'whatsapp_number'}),
            'emp_profile' :  forms.FileInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'emp_profile'}),
            'catagory' :  forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'catagory'}),
            'username': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            # 'c_password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'o_password'}),
            'address': forms.Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'address'}),
            'dob': forms.DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'dob'}),
            'join_date': forms.DateInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'join_date'}),
            'district': forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'district'}),
            'state': forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'state'}),
            'nationality':forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'nationality'}),
            'marital_status':forms.TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'marital_status'}),
        }


class EmergenctResetForm(forms.ModelForm):
      class Meta:
        model = EmergenctContact
        fields = ('primarycontact_name', 'emergency_number', 'relation')
        widgets = {
            'emergency_number': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'emergency_number'}),
            'primarycontact_name':TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'primarycontact_name'}),
            'relation' : TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'relation'}),
        }

class ChangePasswordForm(forms.ModelForm):
      class Meta:
        model = Employees
        fields = ('password','password','password')
        widgets = {
            'password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'o_password'}),
            'password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            'password': PasswordInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'c_password','name':'c_password'}),

        }
