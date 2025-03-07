from django.core.management.commands.runserver import naiveip_re
from django.urls import path
from admin_app import views


urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('user_management', views.user_management, name='user_management'),
    path('facility_management/', views.facility_management, name='facility_management'),
    path('appointment_management/', views.appointment_management, name='appointment_management'),

    # Deletion URLs
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('delete_facility/<int:pk>/', views.delete_facility, name='delete_facility'),
    path('delete_appointment/<int:pk>/', views.delete_appointment, name='admin_delete_appointment'),

]