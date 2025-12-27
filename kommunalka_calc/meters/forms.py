from django import forms

class MeterForm(forms.Form):
    cold_prev = forms.FloatField(label="Холодная вода (предыдущее)")
    cold_curr = forms.FloatField(label="Холодная вода (текущее)")
    hot_prev = forms.FloatField(label="Горячая вода (предыдущее)")
    hot_curr = forms.FloatField(label="Горячая вода (текущее)")
    electricity = forms.FloatField(label="Электричество", required=False)
    internet = forms.FloatField(label="Интернет", required=False)
