from django import forms
from .models import MeterReading


class MeterForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = [
            "cold_prev",
            "cold_curr",
            "hot_prev",
            "hot_curr",
            "electricity",
            "internet",
        ]
        labels = {
            "cold_prev": "Холодная вода (предыдущее)",
            "cold_curr": "Холодная вода (текущее)",
            "hot_prev": "Горячая вода (предыдущее)",
            "hot_curr": "Горячая вода (текущее)",
            "electricity": "Электричество",
            "internet": "Интернет",
        }
