from django.urls import path
from . import views


urlpatterns = [
    path('doctor_dashboard',views.doctor_dashboard,name="doctor_dashboard"),
    path('patient_management', views.patient_management, name='patient_management'),
    path('appointment_schedule', views.appointment_schedule, name='appointment_schedule'),
    path('update_appointment_status/<int:pk>/',views.update_appointment_status,name="update_appointment_status"),
    path('e_prescribing', views.e_prescribing, name='e_prescribing'),
    path('update_prescription/<int:pk>',views.update_prescription,name='update_prescription'),
    path('delete_prescription/<int:pk>/', views.delete_prescription, name='delete_prescription'),
    path('delete_appointment/<int:pk>/', views.delete_appointment, name='delete_appointment'),

]