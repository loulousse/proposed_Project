from django import forms
from . models import *

#COLOR_CHOICES =(
 #   ("1", "Blue"),
  #  ("2", "White"),
#)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userId','fname','lname')

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('route_from','route_to','fare')

class BeepJeepForm(forms.ModelForm):
    class Meta:
        model = BeepJeep
        fields = ('color','capacity','beepStatus')

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticketId','modeOfPayment','validTime')

#class ColorForm(forms.Form):
 #   color_field = forms.ChoiceField(choices = COLOR_CHOICES)