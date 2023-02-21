from django.shortcuts import get_object_or_404
from rest_framework import serializers
from vacancies.models import Vacancy
from accounts.models import Employer, Applicant, Experience
from vacancies.models import Feedback
from pprint import pprint


class VacancySerializer(serializers.ModelSerializer):
	"""Вакансия"""
	# company = serializers.StringRelatedField(read_only=True)

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
	# def get_company(self):
	# 	request = self.context.get('request')
	# 	user = request.user
	# 	company = Employer.objects.get(user_id=user.id)
	# 	print(company, "*" * 79)
	# 	return company


class EmployerCreateSerializer(serializers.ModelSerializer):
	"""Регистрация работодателя"""
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Employer
		fields = "__all__"


class ApplicantCreateSerializer(serializers.ModelSerializer):
	"""Регистрация соискателя"""
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Applicant
		fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
	"""Отклики"""
	class Meta:
		model = Feedback
		fields = ("id", 'vacancy', 'applicant')
		read_only_fields = ('vacancy', 'applicant')

	def validate(self, attrs):
		request = self.context.get('request')
		user = request.user
		applicant = Applicant.objects.get(user_id=user.id)
		vacancy_id = request.parser_context.get('kwargs').get('vacancy_id')
		if Feedback.objects.all().filter(
				applicant=applicant, vacancy=vacancy_id
		).exists():
			raise serializers.ValidationError(
				{'Ошибка': 'Вы уже откликались на эту вакансию'}
			)
		return attrs

	def to_representation(self, instance):
		data = {"feedback_id": instance.id}
		data.update(VacancySerializer(instance.vacancy).data)
		return data


class ShowExperienceSerializer(serializers.ModelSerializer):
	"""Вывод информации об опыте"""
	class Meta:
		model = Experience
		fields = "__all__"


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
			"experience"

		)


class ShowFeedbacksSerializer(serializers.ModelSerializer):
	"""Для просмотра откликов от соискателей"""
	class Meta:
		model = Feedback
		fields = ("applicant", "vacancy")

	def to_representation(self, instance):
		data = {
			"vacancy_id": instance.vacancy.id,
			"vacancy_title": instance.vacancy.title
		}
		data.update(ShowApplicantSerializer(instance.applicant).data)
		return data
