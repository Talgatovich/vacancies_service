from rest_framework import serializers

from accounts.models import Applicant, Employer, Experience
from vacancies.models import Feedback, Vacancy


class ShowEmployerSerializer(serializers.ModelSerializer):
    """Информация о работодателе"""

    class Meta:
        model = Employer
        fields = (
            "company_name",
            "staff_quantity",
            "city",
            "address",
            "phone_number",
            "tg_link",
            "vk_link",
            "about",
            "email",
        )


class VacancySerializer(serializers.ModelSerializer):
    """Информация о вакансии"""

    company = serializers.StringRelatedField()

    class Meta:
        model = Vacancy
        fields = (
            "id",
            "title",
            "salary",
            "description",
            "company",
        )
        read_only_fields = ("company",)


class ExtendedVacancySerializer(serializers.ModelSerializer):
    """Расширенная информация о вакансии"""

    company = ShowEmployerSerializer()

    class Meta:
        model = Vacancy
        fields = (
            "id",
            "title",
            "salary",
            "description",
            "image",
            "company",
        )
        read_only_fields = ("company",)


class EmployerCreateSerializer(serializers.ModelSerializer):
    """
        Регистрация работодателя.
        Внимание!Перед этим необходимо зарегистрировать
        пользователя и получить токен.
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Employer
        fields = (
            "user",
            "company_name",
            "staff_quantity",
            "city",
            "address",
            "phone_number",
            "tg_link",
            "vk_link",
            "about",
            "email",
        )


class ApplicantCreateSerializer(serializers.ModelSerializer):
    """
        Регистрация соискателя.
        Внимание!Перед этим необходимо зарегистрировать
        пользователя и получить токен.
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Applicant
        fields = (
            "user",
            "firstname",
            "lastname",
            "patronymic",
            "email",
            "city",
            "address",
            "phone_number",
            "tg_link",
            "vk_link",
        )


class FeedbackSerializer(serializers.ModelSerializer):
    """Отправка отклика на вакансию"""

    class Meta:
        model = Feedback
        fields = ("id", "vacancy", "applicant")
        read_only_fields = ("vacancy", "applicant")

    def validate(self, attrs):
        request = self.context.get("request")
        user = request.user
        applicant = Applicant.objects.get(user_id=user.id)
        vacancy_id = request.parser_context.get("kwargs").get("vacancy_id")
        if (
            Feedback.objects.all()
            .filter(applicant=applicant, vacancy=vacancy_id)
            .exists()
        ):
            raise serializers.ValidationError(
                {"Ошибка": "Вы уже откликались на эту вакансию"}
            )
        return attrs

    def to_representation(self, instance):
        data = {"feedback_id": instance.id}
        data.update(VacancySerializer(instance.vacancy).data)
        return data


class ShowExperienceSerializer(serializers.ModelSerializer):
    """Вывод информации об опыте работы"""

    class Meta:
        model = Experience
        fields = (
            "id",
            "company_name",
            "start_date",
            "finish_date",
            "job_results",
        )


class ShowApplicantSerializer(serializers.ModelSerializer):
    """Вывод информации о соискателе"""

    experience = ShowExperienceSerializer(read_only=True, many=True)

    class Meta:
        model = Applicant
        fields = (
            "firstname",
            "lastname",
            "patronymic",
            "email",
            "city",
            "address",
            "phone_number",
            "tg_link",
            "vk_link",
            "experience",
        )


class ShowFeedbacksSerializer(serializers.ModelSerializer):
    """Просмотр откликов от соискателей"""

    class Meta:
        model = Feedback
        fields = ("applicant", "vacancy")

    def to_representation(self, instance):
        data = {
            "vacancy_id": instance.vacancy.id,
            "vacancy_title": instance.vacancy.title,
        }
        data.update(ShowApplicantSerializer(instance.applicant).data)
        return data
