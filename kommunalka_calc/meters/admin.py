from django.contrib import admin
from .models import MeterReading

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "cold_prev", "cold_curr",
        "hot_prev", "hot_curr",
        "electricity", "internet",
        "total",
    )

    list_filter = ("created_at",)

    ordering = ("-created_at",)

    readonly_fields = (
        "cold_cost",
        "hot_cost",
        "sewage_cost",
        "total",
        "created_at",
    )

    fieldsets = (
        ("Показания", {
            "fields": (
                ("cold_prev", "cold_curr"),
                ("hot_prev", "hot_curr"),
            )
        }),
        ("Дополнительно", {
            "fields": ("electricity", "internet")
        }),
        ("Результат", {
            "fields": (
                "cold_cost",
                "hot_cost",
                "sewage_cost",
                "total",
                "created_at",
            )
        }),
    )

