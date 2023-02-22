from django_filters import rest_framework as filters

from vacancies.models import Vacancy


class VacancyFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name="salary", lookup_expr="gte")
    max_salary = filters.NumberFilter(field_name="salary", lookup_expr="lte")
    title = filters.CharFilter(lookup_expr="icontains")
    company__company_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Vacancy
        fields = ["salary", "title", "company__company_name"]
