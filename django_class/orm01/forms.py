from django import forms
from .models import address

class addressForm(forms.ModelForm):
    class Meta:
        model = address
        fields = ['my_name', 'my_addr', 'EMAIL']
