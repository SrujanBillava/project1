from django import forms # type: ignore
from .models import Member

class ContactModelForm(forms.ModelForm):
    class Meta:
        model =Member
        fields = ['firstname','lastname', 'phone', 'joined_date']