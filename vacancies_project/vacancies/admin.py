from django.contrib import admin

from .models import Feedback, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "salary",
        "description",
        "image",
        "company",
    )


@admin.register(Feedback)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "applicant",
        "vacancy",
    )
