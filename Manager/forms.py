from django import forms
from .models import tasks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class inputfiled(forms.Form):
    input_text = forms.CharField(max_length=100,label='')

    input_text.widget.attrs.update({"class": "form-control border border-secondary"})
    input_text.widget.attrs.update({"type": "text"})
    input_text.widget.attrs.update({"autocomplete": "off"})
    input_text.widget.attrs.update({"value": ""})


class InputField(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control border border-secondary'})
        }
        labels = {
            "task": ""
        }
        autocomplete = {
            "task":"off"
        }
        #name = {
           # "task":"input_text"
        #}

'''class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField()
    passwrord2 = forms.CharField()

    class Meta:
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control border border-secondary', 'placeholder': 'Username'}),
            'password2': forms.TextInput(attrs={'class': 'form-control border border-secondary', 'placeholder': 'First Name'}),
        }'''


    