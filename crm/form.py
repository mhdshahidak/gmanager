from django import forms
from django.forms.widgets import (
    EmailInput,
    FileInput,
    NumberInput,
    PasswordInput,
    Select,
    Textarea,
    TextInput,
)

from ceo.models import Client

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = (
            "projectname",
            "files",
            "companyname",
            "clientname",
            "email",
            "phone",
            "referredby",
            "type",
            "details",
            "whatsapp",
            "address",
        )

        widgets = {
            "details": Textarea(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Details",
                    "name": "details",
                    "id": "details",
                }
            ),
            "address": Textarea(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Address",
                    "name": "address",
                    "id": "details",
                }
            ),
            "projectname": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Projectname",
                    "name": "projectname",
                }
            ),
            "companyname": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Company Name",
                    "name": "companyname",
                }
            ),
            "clientname": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Client Name",
                    "name": "clientname",
                }
            ),
            "referredby": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Referred By",
                    "name": "referredby",
                    "value": id,
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control bx-inp",
                    "autocomplete": "off",
                    "placeholder": "E-mail",
                    "name": "email",
                }
            ),
            "phone": NumberInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Phone",
                    "name": "phone",
                }
            ),
            "whatsapp": NumberInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "whatsapp",
                    "name": "whatsapp",
                }
            ),
            "files": FileInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": False,
                    "autocomplete": "off",
                    "placeholder": "files",
                    "name": "files",
                }
            ),
            "type": Select(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Select",
                    "name": "Select",
                }
            ),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            "name",
            "companyname",
            "address",
            "email",
            "phone",
            "whatsapp_number",
            "username",
            "password",
        )

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "name",
                    "name": "name",
                }
            ),
            "companyname": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Company Name",
                    "name": "companyname",
                }
            ),
            "address": Textarea(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Address",
                    "name": "address",
                }
            ),
            "username": TextInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Username",
                    "name": "username",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "E-mail",
                    "name": "email",
                }
            ),
            "phone": NumberInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Phone",
                    "name": "phone",
                }
            ),
            "whatsapp_number": NumberInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Whatsapp Number",
                    "name": "whatsapp_number",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "form-control bx-inp",
                    "required": "required",
                    "autocomplete": "off",
                    "placeholder": "Password",
                    "name": "password",
                }
            ),
        }
