from django.contrib import admin
from .models import Contacts, Applicant, Employer, Experience

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
	list_display = (
		"address",
		"phone_number",
		"tg_link",
		"vk_link",
		"email",
	)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
	list_display = (
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
		"contacts",
		"about",
		"is_employer"
	)


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
	list_display = (

		"id",
		"firstname",
		"lastname",
		"patronymic",
		"email",
		"contacts",
		"work_experience",
		"is_employer"
	)