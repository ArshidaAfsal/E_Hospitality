from django import forms
from doctor.models import Prescription, AppointmentSchedule



# Prescription Form
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'



# Appointment Form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentSchedule
        fields = '__all__'