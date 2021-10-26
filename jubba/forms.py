from django import forms
from .models import CostINfo
from django.forms import ModelForm, TextInput, EmailInput,Textarea

class CostINfoCreateForm(forms.ModelForm):
  class Meta:
    model = CostINfo
    fields = ("File_name","compny_name","town_city","phone", "text")
    widgets = {
            'File_name': TextInput(attrs={
                'class': "input1",
                'placeholder': 'File name'
                
                }),
            'compny_name': TextInput(attrs={
                'class': "input1", 
                'placeholder': 'Compny name'
                
                }),
            'town_city': TextInput(attrs={
                'class': "input1", 
                'placeholder': 'Town City'
                }),
            'phone': TextInput(attrs={
                'class': "input1", 
                'placeholder': 'Phone'
                }),
            'text': Textarea(attrs={
                'class': "input1", 
                'placeholder': 'Description'
                
                }),
            
        }

