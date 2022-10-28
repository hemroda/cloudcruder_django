from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput

from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),
        }

    def clean_date(self):
        date_field = self.cleaned_data.get("date")
        if date_field < date.today():
            raise ValidationError("Event cannot be in the past")
        return date_field
