
from django import forms

from .models import *

class PostHornetForm(forms.ModelForm):

    class Meta:
        model = Hornet
        fields = ('lat', 'lng','email','view_dtime')
        
