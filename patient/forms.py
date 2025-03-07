from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from patient.models import *





class PatientRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()






class PatientProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = '__all__'




class AppointmentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        required=False
    )

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }




class MedicalHistoryForm(forms.ModelForm):

    class Meta:
        model = MedicalHistory
        fields = '__all__'
        widgets = {
            'field_name': forms.TextInput(attrs={'class':'form-control'}),
            'textarea_field': forms.Textarea(attrs={'class':'form-control','rows':3}),
        }





class HealthResourceForm(forms.ModelForm):
    class Meta:
        model = HealthResource
        fields = ['title', 'content', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Content', 'rows': 4}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Link (optional)'}),
        }


