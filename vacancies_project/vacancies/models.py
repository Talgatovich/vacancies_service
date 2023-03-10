from django.db import models

from accounts.models import Applicant, Employer


class Vacancy(models.Model):
    """Вакансия"""

    title = models.CharField(
        "Название", max_length=100, help_text="Заполните название вакансии"
    )
    salary = models.PositiveIntegerField(
        "Зарплата", help_text="Заработная плата в рублях"
    )
    description = models.TextField(
        "Описание", max_length=3000, help_text="Заполните описание"
    )
    image = models.ImageField(
        "Картинка", upload_to="vacancy", help_text="Загрузите изображение"
    )
    company = models.ForeignKey(
        Employer, related_name="vacancy", on_delete=models.CASCADE
    )
    created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ("created",)
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"{self.title}"


class Feedback(models.Model):
    """Отклики"""

    vacancy = models.ForeignKey(
        Vacancy, related_name="feedback", on_delete=models.CASCADE
    )
    applicant = models.ForeignKey(
        Applicant, related_name="feedback", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "applicant"], name="unique_feedback"
            )
        ]
