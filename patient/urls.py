from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    # Authentication
    path('PatientRegister', views.PatientRegister.as_view(), name='patient_register'),
    path('', views.PatientLogin, name='patient_login'),
    path('logout/', views.patient_logout, name='patient_logout'),

    # Profile
    path('PatientProfileCreate/',views.PatientProfileCreate,name="PatientProfileCreate"),
    path('ProfileView/',views.ProfileView,name='ProfileView'),
    path('PatientProfileUpdate/',views.PatientProfileUpdate,name='PatientProfileUpdate'),

    # Appointments
    path('book_appointments/', views.book_appointment, name='book_appointment'),
    # path('appointments/', views.view_appointments, name='view_appointments'),

    # Billing and Payments
    path('create-checkout-session/<int:billing_id>/', views.create_checkout_session, name="create_checkout_session"),
    path('payment-success/<int:billing_id>/', views.payment_success, name='payment_success'),
    path('payment-cancel/<int:billing_id>/', views.payment_cancel, name='payment_cancel'),

    # Medical History
    path('MedicalHistoryCreate/',views.MedicalHistoryCreate,name='MedicalHistoryCreate'),
    path('medical-history/', views.view_medical_history, name='view_medical_history'),


    # Health Education Resources
    path('view_health-resources/', views.view_health_resources, name='view_health_resources'),
    path('health_resources/',views.health_resources,name='health_resources'),
]