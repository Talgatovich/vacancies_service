from django.db import models
from accounts.models import Applicant, Employer


class Vacancy(models.Model):
	"""Вакансия"""
	title = models.CharField("Название", max_length=100)
	salary = models.PositiveIntegerField("Зарплата")
	description = models.CharField("Описание", max_length=3000)
	image = models.ImageField("Картинка", upload_to="vacancy")
	company = models.ForeignKey(
		Employer,
		related_name='vacancy',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return f"{self.title}"


class Feedback(models.Model):
	"""Отклики"""
	vacancy = models.ForeignKey(
		Vacancy,
		related_name='feedback',
		on_delete=models.CASCADE
	)
	applicant = models.ForeignKey(
		Applicant,
		related_name='feedback',
		on_delete=models.CASCADE
	)