import stripe
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.models import User
from .models import Appointment, MedicalHistory, Billing, HealthResource


# Create your views here.




# Patient Registration
class PatientRegister(CreateView):

    template_name = 'patient/patient_register.html'
    form_class = PatientRegistrationForm
    model = User
    success_url = reverse_lazy("patient_login")




# Patient Login
def PatientLogin(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)

            if not Patient.objects.filter(username=user).exists():
                return redirect('PatientProfileCreate')

            return redirect('index')

        else:
            messages.error(request,"Invalid username or password")
            return redirect('patient_login')
    return render(request, 'patient/patient_login.html')




# ProfileCreate
def PatientProfileCreate(request):
    profile=Patient.objects.all()
    if request.method=='POST':
        form=PatientProfileForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')

            if password1 != password2:
                messages.error(request,"Passwords do not match!")
                return render(request,"patient/patient_profile.html",{"form":form,"profile":profile})
            if Patient.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return render(request, "patient/patient_profile.html", {"form": form, "profile": profile})

            form.save()
            messages.success(request,"Profile Created Successfully!")
            return redirect('index')
        else:
            messages.error(request,"Invalid data submitted!")
    else:
        form=PatientProfileForm()
    return render(request,"patient/patient_profile.html",{"form":form,"profile":profile})



# Profile View
@login_required
def ProfileView(request):
    patient=Patient.objects.get(id=request.user.id)

    return render(request,"patient/profileview.html",{"patient":patient})



# Update Patient Profile
@login_required
def PatientProfileUpdate(request):
    patient = get_object_or_404(Patient, id=request.user.id)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('index')
        else:
            messages.error(request, "Error updating profile!")
    else:
        form = PatientProfileForm(instance=patient)

    return render(request, "patient/update_patient_profile.html", {"form": form})





# Appointment Booking
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()

            billing = Billing.objects.create(
                patient=request.user,
                amount=appointment.fee,
                status='Unpaid'
            )
            return redirect('create_checkout_session', billing_id=billing.id)
        else:
            form = AppointmentForm(request.POST)
    else:
        form = AppointmentForm()
    return render(request, 'patient/book_appointment.html', {'form': form})


# View All Appointments
# def view_appointments(request):
#     appointments = Appointment.objects.filter(patient=request.user.patient)
#     return render(request, 'patient/view_appointments.html', {'appointments': appointments})





# Create Medical History
@login_required
def MedicalHistoryCreate(request):
    if request.method == 'POST':
        form=MedicalHistoryForm(request.POST)
        if form.is_valid():
            medical_history = form.save(commit=False)
            medical_history.patient = request.user
            medical_history.save()
            return redirect('index')
    else:
        form=MedicalHistoryForm()
    return render(request,"patient/add_medical_history.html",{"form":form})




# Medical History
@login_required
def view_medical_history(request):
    medical_history = MedicalHistory.objects.filter(patient=request.user)
    patients = Patient.objects.all()
    return render(request, 'patient/medical_history.html', {'medical_history': medical_history,'patients':patients})





# Stripe Payment
def create_checkout_session(request, billing_id):

    billing = get_object_or_404(Billing, id=billing_id, patient=request.user)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'GET':
        try:
            checkout_session=stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'INR',
                        'unit_amount': int(billing.amount * 100),
                        'product_data': {
                            'name': f'Appointment Payment for {billing.patient.username}'
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('payment_success',args=[billing_id])),
                cancel_url=request.build_absolute_uri(reverse('payment_cancel',args=[billing_id])),
            )

            billing.stripe_payment_intent=checkout_session.payment_intent
            billing.save()

            return redirect(checkout_session.url, code=303)

        except Exception as e:
            return HttpResponse(f'Error occurred: {str(e)}', status=500)

    return HttpResponse('Invalid request method.', status=405)






# Payment Success
def payment_success(request, billing_id):
    billing = get_object_or_404(Billing, id=billing_id, patient=request.user)
    billing.status = 'Paid'
    billing.save()
    return render(request, 'patient/payment_success.html', {'billing': billing})





# Payment Cancel
def payment_cancel(request, billing_id):
    return render(request, 'patient/payment_cancel.html')





# Health Education Resources
def view_health_resources(request):
    resources = HealthResource.objects.all()
    return render(request, 'patient/view_health_resources.html', {'resources': resources})


# Create Health Resources
def health_resources(request):
    if request.method == 'POST':
        form=HealthResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=HealthResourceForm()
    return render(request,"patient/health_resources.html",{"form":form})



# Patient Logout
def patient_logout(request):
    logout(request)
    return redirect('patient_login')



def index(request):
    return render(request,'patient/index.html')


