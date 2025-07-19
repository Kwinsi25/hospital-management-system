from rest_framework import serializers
from .models import User, Slot, Appointment
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer): # Serializer for user registration
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class LoginSerializer(serializers.Serializer): # Serializer for user login
    """Serializer for user login."""
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

class SlotSerializer(serializers.ModelSerializer): # Serializer for appointment slots
    """Serializer for appointment slots."""
    class Meta:
        model = Slot
        fields = '__all__'
        read_only_fields = ['doctor', 'is_booked']


class AppointmentSerializer(serializers.ModelSerializer): # Serializer for appointments
    """Serializer for appointments."""
    doctor_name = serializers.SerializerMethodField() # To get doctor's email
    patient_name = serializers.SerializerMethodField()  # To get patient's email
    slot_details = SlotSerializer(source='slot') # Nested serializer for slot details

    class Meta:
        model = Appointment
        fields = ['id', 'doctor_name', 'patient_name', 'slot_details', 'status']

    def get_doctor_name(self, obj):
        return obj.slot.doctor.email

    def get_patient_name(self, obj):
        return obj.patient.email
