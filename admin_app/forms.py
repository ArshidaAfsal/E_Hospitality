from django import forms
from admin_app.models import Facility, UserManagement, AppointmentManagement


# Form for User Management
class UserForm(forms.ModelForm):
    class Meta:
        model = UserManagement
        fields = ['username','email','role','is_active']




# Form for Facility Management
class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name','location','department','resources']



# Form for Appointment Management
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentManagement
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }