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


        

