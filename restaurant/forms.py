from .models import Booking
from django import forms 


class BookingForm(forms.ModelForm):
    model = Booking
    fields ="__all__"
    