from django.shortcuts import get_object_or_404
from rest_framework import serializers
from vacancies.models import Vacancy
from accounts.models import Employer, Applicant
from vacancies.models import Feedback
from pprint import pprint


class VacancySerializer(serializers.ModelSerializer):
	company = serializers.StringRelatedField(read_only=True)

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


class EmployerCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Employer
		fields = "__all__"


class ApplicantCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Applicant
		fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):

	class Meta:
		model = Feedback
		fields = ('vacancy', 'applicant')
		read_only_fields = ('vacancy', 'applicant')

	def to_representation(self, instance):
		return VacancySerializer(instance.vacancy).data


