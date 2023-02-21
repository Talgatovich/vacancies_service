from pprint import pprint

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, status
from vacancies.models import Vacancy
from .serializers import VacancySerializer, EmployerCreateSerializer, ApplicantCreateSerializer, FeedbackSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics
from accounts.models import Employer, Applicant
from vacancies.models import Feedback
from django.shortcuts import get_object_or_404

CREATED = status.HTTP_201_CREATED


class VacancyAPIView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'index.html'
	serializer_class = VacancySerializer

	def get(self, request):
		queryset = Vacancy.objects.all()
		serializer = VacancySerializer(queryset, many=True).data
		return Response({'vacancies': serializer})


class VacancyDetail(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'vacancy_detail.html'
	serializer_class = VacancySerializer

	def get(self, request, pk):
		vacancy = Vacancy.objects.all().get(pk=pk)
		serializer = VacancySerializer(vacancy).data
		return Response({'vacancy': serializer})


class EmployerRegistration(generics.CreateAPIView):
	"""Регистрация работодателя"""
	queryset = Employer.objects.all()
	serializer_class = EmployerCreateSerializer


class ApplicantRegistration(generics.CreateAPIView):
	"""Регистрация соискателя"""
	queryset = Applicant.objects.all()
	serializer_class = ApplicantCreateSerializer


class VacancyViewSet(ModelViewSet):
	"""Вакансии"""
	queryset = Vacancy.objects.all()
	serializer_class = VacancySerializer


class SendFeedBackView(ModelViewSet):
	"""Отправка отклика работодателю"""

	# queryset = Feedback.objects.all()
	serializer_class = FeedbackSerializer

	def get_queryset(self):
		user = self.request.user
		applicant = get_object_or_404(Applicant, user_id=user.id)
		queryset = Feedback.objects.all().filter(applicant_id=applicant)
		return queryset
	def perform_create(self, serializer):
		user = self.request.user
		applicant = get_object_or_404(Applicant, user_id=user.id)
		vacancy_id = self.kwargs.get('vacancy_id')
		vacancy = get_object_or_404(Vacancy, id=vacancy_id)
		serializer.save(applicant_id=applicant.id, vacancy_id=vacancy.id)

	def validate(self, attrs):
		print(self.__dict__)
		print(attrs.__dict__)
		return attrs


