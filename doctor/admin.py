from django.contrib import admin
from doctor.models import Prescription,AppointmentSchedule

# Register your models here.
admin.site.register(Prescription)
admin.site.register(AppointmentSchedule)
