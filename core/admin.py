from django.contrib import admin
from .models import User, Slot, Appointment 

@admin.register(User)
class UserAdmin(admin.ModelAdmin): # Custom admin for User model
    """
    Custom admin for User model to manage users in the admin interface. 
    """
    list_display = ['id', 'email', 'username', 'role']  
    list_filter = ['role']
    search_fields = ['email', 'username']

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin): # Custom admin for Slot model
    """
    Custom admin for Slot model to manage appointment slots in the admin interface.
    """
    list_display = ['id', 'doctor', 'date', 'start_time', 'end_time']
    list_filter = ['doctor', 'date']
    search_fields = ['doctor__email']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin): # Custom admin for Appointment model
    """
    Custom admin for Appointment model to manage appointments in the admin interface.
    """
    list_display = ['id', 'patient', 'slot', 'status']
    list_filter = ['status']
    search_fields = ['patient__email', 'slot__doctor__email']
