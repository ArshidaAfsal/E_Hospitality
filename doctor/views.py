from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from doctor.models import Prescription, AppointmentSchedule
from doctor.forms import PrescriptionForm, AppointmentForm
from patient.models import Patient, MedicalHistory, User, Appointment


# Create your views here.


def doctor_dashboard(request):
    return render(request, 'doctor/doctor_dashboard.html')


# Patient Management
def patient_management(request):
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    medical_historys = MedicalHistory.objects.all()
    return render(request, 'doctor/patient_management.html', {'patients': patients,'medical_historys':medical_historys,'appointments':appointments})




# Appointment schedule
def appointment_schedule(request):
    appointments = Appointment.objects.select_related('patient').all()  # Fetch all patient appointments
    return render(request, 'doctor/appointment_schedule.html', {'appointments': appointments})


@require_POST
def update_appointment_status(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    status = request.POST.get('status')
    if status in ['Scheduled', 'Rescheduled']:
        appointment.status = status
        appointment.save()
    return redirect('appointment_schedule')





# E-Prescribing
def e_prescribing(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e_prescribing')
    else:
        form = PrescriptionForm()
    prescriptions = Prescription.objects.all()
    return render(request, 'doctor/e_prescribing.html', {'form': form, 'prescriptions': prescriptions})



# Update View
def update_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('e_prescribing')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'doctor/update_prescription.html', {'form': form})


# Delete Prescription
def delete_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    prescription.delete()
    return redirect('e_prescribing')




# Delete Appointment
def delete_appointment(request, pk):
    appointment = get_object_or_404(AppointmentSchedule, pk=pk)
    appointment.delete()
    return redirect('appointment_schedule')