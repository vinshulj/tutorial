from django import forms
from .models import Email
class EmailForm(forms.ModelForm):
    class Meta:
        Model=Email
        fields=["__all__"]