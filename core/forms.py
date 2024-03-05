from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Name'}),
            'surname':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Surname'}),
            'father_name':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Father Name'}),
            'address':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Address'}),
            'send_type':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Sending Type'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Email'}),
            # 'message':forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Message'}),
            # 'file':forms.FileInput(),
        }