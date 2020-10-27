from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TextInput
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "telephone": TextInput(attrs={"type": "telephone"}),
            "date": DateInput(attrs={"type": "date"}),
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Date cannot be in the past")
        return d

