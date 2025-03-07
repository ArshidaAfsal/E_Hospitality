from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Patient(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)



class Appointment(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    gender = models.CharField(max_length=100,choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    department = models.CharField(max_length=300,choices=[('General Medicine','General Medicine'),('Cardiology','Cardiology'),('Pediatrics','Pediatrics'),('Orthopedics','Orthopedics'),
                                                          ('Gastrology','Gastrology'),('Physiotherapist','Physiotherapist'),('Neurology','Neurology'),('Gynaecologist','Gynaecologist')])
    fee = models.IntegerField(default=400)
    status_choices = [('Pending','Pending'),('Confirmed','Confirmed'),('Completed','Completed'),('Cancelled','Cancelled')]
    status = models.CharField(max_length=20,choices=status_choices,default='Pending')
    reason = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"Appointment with {self.doctor_name} on {self.date} at {self.time}"



class MedicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField(blank=True, null=True)
    treatment_history = models.TextField()
    date = models.DateField(auto_now_add=True)



class Billing(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Unpaid')
    stripe_payment_intent = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"Billing for {self.patient.username} - {self.amount} INR"



class HealthResource(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)