from django.db import models
from patient.models import User,Appointment
# Create your models here.



# Appointment Schedule Model
class AppointmentSchedule(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Appointment,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')

    def _str_(self):
        return f"Appointment with {self.patient} on {self.date}"



# E-Prescription Model
class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)
    prescribed_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Prescription for {self.patient} - {self.medication_name}"