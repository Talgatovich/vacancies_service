from django.contrib.auth.models import User
from django.db import models


class Employer(models.Model):
    """Работодатель."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer")
    email = models.EmailField("Почта")
    company_name = models.CharField("Название компании", max_length=150)
    staff_quantity = models.PositiveIntegerField("Количество сотрудников")
    city = models.CharField("Город", max_length=50)
    address = models.CharField("Адрес", max_length=300, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=11, blank=True)
    tg_link = models.CharField("Ссылка на телеграм", max_length=100, blank=True)
    vk_link = models.CharField("Ссылка в вк", max_length=100, blank=True)
    about = models.CharField("О компании", max_length=2000)

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"

    def __str__(self):
        return f"{self.company_name}"


class Applicant(models.Model):
    """Соискатель."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="applicant"
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

    class Meta:
        verbose_name = "Соискатель"
        verbose_name_plural = "Соискатели"

    def __str__(self):
        return f"{self.firstname}"


class Experience(models.Model):
    """Опыт работы"""

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name="experience",
        verbose_name="Соискатель",
    )
    company_name = models.CharField("Название компании", max_length=150)
    start_date = models.DateField("Дата начала работы")
    finish_date = models.DateField("Дата окончания работы")
    job_results = models.CharField("Результаты работы", max_length=300)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"

    def __str__(self):
        return f"{self.company_name}"
