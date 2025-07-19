from django.urls import path
from .views import *

urlpatterns = [
    path('', api_root), 
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('slots/create/', SlotCreateView.as_view()),
    path('slots/mine/', MySlotsView.as_view()),
    path('slots/available/', AvailableSlotsView.as_view()),

    path('appointments/book/', BookAppointmentView.as_view()),
    path('appointments/', AppointmentsView.as_view()),
]
