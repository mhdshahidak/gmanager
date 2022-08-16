
from django import forms
from .models import *
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput,PasswordInput,DateInput
 

class PraposalpdfForm(forms.ModelForm):
    class Meta:
        model = Praposalpdf
        fields = ('praposalpdf',)
      
        widgets = {
            'praposalpdf': FileInput(attrs={'class': 'form-control', 'placeholder':'Praposal Pdf','name':'praposalpdf','required':'required'}),
        }