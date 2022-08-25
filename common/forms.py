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
        exclude = ('status', '')
        Widget = {
            'name': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'name'}),
            'employee_id': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'employee_id','name':'employee_id'}),
            'email': EmailInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off', 'placeholder':'E-mail','name':'email'}),
            'phone': NumberInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Phone','name':'phone'}),
            'whatsapp_number': NumberInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'whatsapp_number','name':'whatsapp_number'}),
            'emp_profile' : FileInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off','name':'file','id':'files'}),
            'catagory' : Select(attrs={'class': 'form-control bx-inp', 'required': 'required','name':'catagory','name':'catagory'}),
            'username': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'username','name':'username'}),
            'password': PasswordInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'password','name':'password'}),
            # 'c_password': PasswordInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'c_password','name':'c_password'}),
            'address': Textarea(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'address','name':'address'}),
            'dob': DateInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'dob','name':'dob','type':'date'}),
            'join_date': DateInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'join_date','name':'join_date','type':'date'}),
            'district': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'district'}),
            'state': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'state'}),
            'nationality':TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'nationality'}),
            'marital_status':TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'marital_status'}),
        }

class EmergenctResetForm(forms.ModelForm):
    class Meta:
        model = EmergenctContact
        fields = ('primarycontact_name', 'emergency_number', 'relation')
        widget = {
            'emergency_number': TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'emergency_number'}),
            'primarycontact_name':TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'primarycontact_name'}),
            'relation' : TextInput(attrs={'class': 'form-control bx-inp', 'autocomplete':'off', 'placeholder':'Name','name':'relation'}),
        }
