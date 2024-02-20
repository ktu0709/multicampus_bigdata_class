from django import forms
from .models import YourModel


class MyForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'



