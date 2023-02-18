from rest_framework import serializers
from vacancies.models import Vacancy


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