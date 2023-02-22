from django.contrib import admin

from .models import Applicant, Employer, Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "applicant",
        "company_name",
        "start_date",
        "finish_date",
        "job_results",
    )


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "company_name",
        "staff_quantity",
        "city",
        "about",
    )


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstname",
        "lastname",
        "patronymic",
        "email",
    )
