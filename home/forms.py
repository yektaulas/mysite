from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'dept']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Name "}),
            'email': forms.TextInput(attrs={'placeholder': "E-mail"}),
            'message': forms.Textarea(attrs={'placeholder': "Message", 'rows': 6})
        }