from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# User = get_user_model()


# class Contacts(models.Model):
# 	"""Контакты."""
# 	address = models.CharField("Адрес", max_length=300)
# 	phone_number = models.CharField("Номер телефона", max_length=11)
# 	tg_link= models.CharField("Ссылка на телеграм", max_length=300)
# 	vk_link = models.CharField("Ссылка в вк", max_length=300)
# 	email = models.EmailField("Эл.почта")
#
# 	def __str__(self):
# 		return f"{self.phone_number}"


class Experience(models.Model):
	"""Опыт работы"""
	company_name = models.CharField("Название компании", max_length=150)
	start_date = models.DateField("Дата начала работы")
	finish_date = models.DateField("Дата окончания работы")
	job_results = models.CharField("Результаты работы", max_length=300)

	def __str__(self):
		return f"{self.company_name}"


class Employer(models.Model):
	"""Работодатель."""
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name='employer'
	)
	email = models.EmailField("Почта")
	company_name = models.CharField("Название компании", max_length=150)
	staff_quantity = models.PositiveIntegerField("Количество сотрудников")
	city = models.CharField("Город", max_length=50)
	address = models.CharField("Адрес", max_length=300, blank=True)
	phone_number = models.CharField("Номер телефона", max_length=11, blank=True)
	tg_link = models.CharField("Ссылка на телеграм", max_length=100, blank=True)
	vk_link = models.CharField("Ссылка в вк", max_length=100, blank=True)
	about = models.CharField("О компании", max_length=2000)
	is_employer = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.company_name}"


class Applicant(models.Model):
	"""Соискатель."""
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name='applicant'
	)
	firstname = models.CharField("Имя", max_length=150)
	lastname = models.CharField("Фамилия", max_length=150)
	patronymic = models.CharField("Отчество", max_length=150)
	email = models.EmailField("Почта")
	city = models.CharField("Город", max_length=50)
	address = models.CharField("Адрес", max_length=300, blank=True)
	phone_number = models.CharField("Номер телефона", max_length=11, blank=True)
	tg_link = models.CharField("Ссылка на телеграм", max_length=100, blank=True)
	vk_link = models.CharField("Ссылка в вк", max_length=100, blank=True)
	work_experience = models.ForeignKey(
		Experience,
		on_delete=models.SET_NULL,
		related_name='experience',
		null=True
	)
	is_employer = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.firstname}"

