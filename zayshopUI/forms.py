from django.forms import forms
from .models import ContactUsForm


class ContactForm(forms.ModelForm):
    model = ContactUsForm
    fields = '__all__'