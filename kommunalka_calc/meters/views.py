from django.shortcuts import render
from .forms import MeterForm
from .models import MeterReading

TARIFF_COLD = 65.77
TARIFF_HOT = 322.5
TARIFF_SEWAGE = 51.62

def calculate(request):
    result = None

    if request.method == "POST":
        form = MeterForm(request.POST)
        if form.is_valid():
            cold_prev = form.cleaned_data["cold_prev"]
            cold_curr = form.cleaned_data["cold_curr"]
            hot_prev = form.cleaned_data["hot_prev"]
            hot_curr = form.cleaned_data["hot_curr"]
            electricity = form.cleaned_data.get("electricity") or 0
            internet = form.cleaned_data.get("internet") or 0

            cold_used = cold_curr - cold_prev
            hot_used = hot_curr - hot_prev
            sewage_used = cold_used + hot_used

            cold_cost = cold_used * TARIFF_COLD
            hot_cost = hot_used * TARIFF_HOT
            sewage_cost = sewage_used * TARIFF_SEWAGE

            total = cold_cost + hot_cost + sewage_cost + electricity + internet

            MeterReading.objects.create(
                cold_prev=cold_prev,
                cold_curr=cold_curr,
                hot_prev=hot_prev,
                hot_curr=hot_curr,
                electricity=electricity,
                internet=internet,
                cold_cost=cold_cost,
                hot_cost=hot_cost,
                sewage_cost=sewage_cost,
                total=total,
            )

            result = {
                "cold_cost": round(cold_cost, 2),
                "hot_cost": round(hot_cost, 2),
                "sewage_cost": round(sewage_cost, 2),
                "electricity": electricity,
                "internet": internet,
                "total": round(total, 2),
            }
    else:
        form = MeterForm()

    return render(request, "calc.html", {"form": form, "result": result})


def history(request):
    records = MeterReading.objects.order_by('-created_at')
    return render(request, "history.html", {"records": records})
