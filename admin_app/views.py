from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from admin_app.models import UserManagement, Facility, AppointmentManagement
from admin_app.forms import UserForm, FacilityForm, AppointmentForm

# Create your views here.


def admin_dashboard(request):
    return render(request, 'admin_app/admin_dashboard.html')


# User Management
def user_management(request):
    users = UserManagement.objects.all()
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_management')
    return render(request, 'admin_app/user_management.html', {'form': form, 'users': users})


# Facility Management
def facility_management(request):
    facilities = Facility.objects.all()
    form = FacilityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'admin_app/facility_management.html', {'form': form, 'facilities': facilities})


# Appointment Management
def appointment_management(request):
    appointments = AppointmentManagement.objects.all()
    form = AppointmentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')

    return render(request, 'admin_app/appointment_management.html', {'form': form, 'appointments': appointments})


# User Deletion
def delete_user(request, pk):
    user = get_object_or_404(UserManagement, pk=pk)
    user.delete()
    return redirect('user_management')


# Facility Deletion
def delete_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    facility.delete()
    return redirect('facility_management')


# Appointment Deletion
def delete_appointment(request, pk):
    appointments = get_object_or_404(AppointmentManagement, pk=pk)
    appointments.delete()
    return redirect('appointment_management')