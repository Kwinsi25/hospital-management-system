from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import User, Slot, Appointment
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request): # API root view
    """
    API root view that provides a welcome message and available routes. 
    """
    return Response({
        "status": 200,
        "message": "Welcome to Hospital Management API",
        # "routes": {
        #     "Register": "/api/register/",
        #     "Login": "/api/login/",
        #     "Logout": "/api/logout/",
        #     "Create Slot": "/api/slots/create/",
        #     "My Slots": "/api/slots/mine/",
        #     "Available Slots": "/api/slots/available/",
        #     "Book Appointment": "/api/appointments/book/",
        #     "Appointments": "/api/appointments/",
        # }
    })

class RegisterView(generics.CreateAPIView): # View for user registration
    """
    View for user registration that allows users to create an account.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView): # View for user login
    """
    View for user login that allows users to authenticate and receive a token.
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": 200, "message": "Login successful", "token": token.key})

class LogoutView(APIView): # View for user logout
    """
    View for user logout that allows users to invalidate their token.
    """
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"status": 200, "message": "Logged out successfully"})

class SlotCreateView(generics.CreateAPIView): # View for creating appointment slots
    """
    View for creating appointment slots that allows doctors to create slots.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SlotSerializer

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.role != 'doctor':
            return Response({"status": 403, "message": "Only doctors can create slots"}, status=403)
        return super().create(request, *args, **kwargs)

class MySlotsView(generics.ListAPIView): # View for listing slots created by the logged-in doctor
    """
    View for listing appointment slots created by the logged-in doctor.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SlotSerializer

    def get_queryset(self):
        return Slot.objects.filter(doctor=self.request.user)

class AvailableSlotsView(generics.ListAPIView): # View for listing available appointment slots
    """
    View for listing available appointment slots that are not booked.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SlotSerializer
    queryset = Slot.objects.filter(is_booked=False)

class BookAppointmentView(APIView): # View for booking an appointment  
    """
    View for booking an appointment that allows patients to book available slots.
    """
    def post(self, request):
        slot_id = request.data.get('slot_id')
        try:
            slot = Slot.objects.get(id=slot_id, is_booked=False)
        except Slot.DoesNotExist:
            return Response({"status": 404, "message": "Slot not available"}, status=404)

        if request.user.role != 'patient':
            return Response({"status": 403, "message": "Only patients can book appointments"}, status=403)

        slot.is_booked = True
        slot.save()

        appointment = Appointment.objects.create(slot=slot, patient=request.user)
        return Response({"status": 200, "message": "Appointment booked", "data": AppointmentSerializer(appointment).data})

class AppointmentsView(generics.ListAPIView): # View for listing appointments
    """
    View for listing appointments that allows users to view their appointments.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return Appointment.objects.filter(slot__doctor=user)
        return Appointment.objects.filter(patient=user)
