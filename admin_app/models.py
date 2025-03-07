from django.db import models
from patient.models import User
from multiselectfield import MultiSelectField

# Create your models here.



# User Model for User Management
class UserManagement(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient'),('Staff','Staff')])
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.username





# Facility Model for Facility Management
# Department Choices
DEPARTMENT_CHOICES = [
    ('Emergency Medicine', 'Emergency Medicine'),
    ('Cardiology', 'Cardiology'),
    ('Pediatrics', 'Pediatrics'),
    ('Orthopedics', 'Orthopedics'),
    ('Radiology', 'Radiology'),
    ('Oncology', 'Oncology'),
    ('General Surgery', 'General Surgery'),
    ('Physiotherapy', 'Physiotherapy'),
    ('Neurology', 'Neurology'),
    ('Gastroenterology', 'Gastroenterology'),
]

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    department = MultiSelectField(choices=DEPARTMENT_CHOICES)
    resources = models.TextField()

    def _str_(self):
        return self.name

# Appointment Model for Appointment Management
class AppointmentManagement(models.Model):
    patient_name = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])

    def _str_(self):
        return f"{self.patient_name} with {self.doctor_name} on {self.appointment_date}"
