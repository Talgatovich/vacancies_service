from django import forms
from vacancies.models import Vacancy


class VacancyCreationForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        # fields = "__all__"
        exclude = ('company',)