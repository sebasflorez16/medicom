
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=200, required=True)
    email = forms.EmailField(label='Email', required=True)
    site = forms.CharField(label='website', required=False)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea) ## el widget emula lel TextaField en models. pero esto es una equiteta html. amplia el area del forms/content