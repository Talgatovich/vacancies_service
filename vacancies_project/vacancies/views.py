from django.shortcuts import render
from vacancies.models import Vacancy


def index(request):
	template = "index.html"
	vacancies = Vacancy.objects.all()
	return render(request, template, {'vacancies': vacancies})


def vacancy_detail(request, pk):
	template = "vacancy_detail.html"
	vacancy = Vacancy.objects.select_related("company").get(pk=pk)
	# about =

	return render(request, template, {'vacancy': vacancy})
