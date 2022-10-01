from django import forms
from django.forms.widgets import DateInput, FileInput, Select, TextInput

from .models import Praposalpdf, Project


class PraposalpdfForm(forms.ModelForm):
    class Meta:
        model = Praposalpdf
        fields = ("praposalpdf",)

        widgets = {
            "praposalpdf": FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Praposal Pdf",
                    "name": "praposalpdf",
                    "required": "required",
                }
            ),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("projectname", "endingdate", "starteddate", "projecttype", "client")

        widgets = {
            "projectname": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Projectname",
                    "name": "projectname",
                }
            ),
            "endingdate": DateInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "endingdate",
                    "name": "endingdate",
                    "type": "date",
                }
            ),
            "starteddate": DateInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "starteddate",
                    "name": "starteddate",
                    "type": "date",
                }
            ),
            "projecttype": Select(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "name": "projecttype",
                    "name": "projecttype",
                }
            ),
            "client": Select(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "name": "Client",
                    "name": "client",
                }
            ),
        }
