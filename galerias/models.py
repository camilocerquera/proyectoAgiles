from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput,TextInput,Textarea

#Tabla de imagenes
class Urls(models.Model):
 url=models.CharField(max_length=2048)
 date=models.DateTimeField()
 user=models.CharField(max_length=16)
 title =models.CharField(max_length=250) 
 description =models.CharField(max_length=2048)

#Tabla de registro de contacto
class Contact(models.Model):
 name=models.CharField(max_length=300)
 email=models.EmailField(max_length=100)
 msg=models.CharField(max_length=2048)
 date =models.DateTimeField(blank=True, null=True) 
 
#Formularios customizados
class UrlsForm(forms.Form):
	url 							= forms.CharField(max_length=2048,required=True,widget=TextInput)
	title							= forms.CharField(max_length=2048, required=True,widget=TextInput)
	description						= forms.CharField(max_length=2048, required=True,widget=Textarea(attrs={'rows':4, 'cols':19}))

class ContactForm(forms.Form):
	name 							= forms.CharField(max_length=300,required=True,widget=TextInput)
	email							= forms.EmailField(max_length=100,required=True)
	msg							= forms.CharField(max_length=2048,required=True,widget=Textarea(attrs={'rows':4, 'cols':30}))
