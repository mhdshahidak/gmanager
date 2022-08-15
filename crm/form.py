from optparse import Option
from django import forms
from .models import *
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput,PasswordInput,DateInput
 

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('projectname','files','companyname','clientname','email','phone','referredby','type','details','whatsapp')
      
        widgets = {
            'details': Textarea(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Details','name':'details','id':'details'}),
            'projectname': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Projectname','name':'projectname'}),
            'companyname': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Company Name','name':'companyname'}),
            'clientname': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Client Name','name':'clientname'}),
            'referredby': TextInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Referred By','name':'referredby','value':id}),
            'email': EmailInput(attrs={'class': 'form-control bx-inp', 'required': 'required', 'autocomplete':'off', 'placeholder':'E-mail','name':'email'}),
            'phone': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Phone','name':'phone'}),
            'whatsapp': NumberInput(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'whatsapp','name':'whatsapp'}),
            'files': FileInput(attrs={'class': 'form-control bx-inp','autocomplete':'off', 'placeholder':'files','name':'files'}),
            'type': Select(attrs={'class': 'form-control bx-inp','required': 'required', 'autocomplete':'off', 'placeholder':'Select','name':'Select'}),
        }