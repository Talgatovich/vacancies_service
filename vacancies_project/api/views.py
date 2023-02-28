from django.shortcuts import get_object_or_404
from django_filters import rest_framework as django_filters
from rest_framework import filters, generics
from rest_framework.viewsets import ModelViewSet

from accounts.models import Applicant, Employer, Experience
from vacancies.models import Feedback, Vacancy

from .filters import VacancyFilter
from .mixins import CreateViewSet, ListRetrieveDestroyViewSet, ListRetrieveViewSet
from .permissions import IsApplicant, IsEmployer, IsEmployerOrReadOnly
from .serializers import (
    ApplicantCreateSerializer,
    EmployerCreateSerializer,
    ExtendedVacancySerializer,
    FeedbackSerializer,
    ShowExperienceSerializer,
    ShowFeedbacksSerializer,
    VacancySerializer,
)


class EmployerRegistration(generics.CreateAPIView):
    """
    Регистрация работодателя.
    Внимание!Перед этим необходимо зарегистрировать
    пользователя и получить токен.
    """

    queryset = Employer.objects.all()
    serializer_class = EmployerCreateSerializer


class ApplicantRegistration(generics.CreateAPIView):
    """
    Регистрация соискателя.
    Внимание!Перед этим необходимо зарегистрировать
    пользователя и получить токен.
    """

    queryset = Applicant.objects.all()
    serializer_class = ApplicantCreateSerializer


class VacancyViewSet(ModelViewSet):
    """Вакансии"""

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = VacancyFilter
    filterset_fields = ("salary", "title", "company__company_name")
    search_fields = ("title",)

    def perform_create(self, serializer):
        user = self.request.user
        company = get_object_or_404(Employer, user_id=user.id)
        serializer.save(company=company)

    def get_serializer_class(self):
        action_list = ["create", "list"]
        if self.action in action_list:
            return VacancySerializer
        return ExtendedVacancySerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsEmployer]
        else:
            permission_classes = [IsEmployerOrReadOnly]
        return [permission() for permission in permission_classes]


class SendFeedBackViewSet(CreateViewSet):
    """Отправка отклика работодателю"""

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsApplicant]

    def perform_create(self, serializer):
        user = self.request.user
        applicant = get_object_or_404(Applicant, user_id=user.id)
        vacancy_id = self.kwargs.get("vacancy_id")
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        serializer.save(applicant_id=applicant.id, vacancy_id=vacancy.id)


class ApplicantFeedBacksViewSet(ListRetrieveDestroyViewSet):
    """Отклики соискателя"""

    serializer_class = FeedbackSerializer
    permission_classes = [IsApplicant]

    def get_queryset(self):
        user = self.request.user
        applicant = get_object_or_404(Applicant, user_id=user.id)
        queryset = Feedback.objects.all().filter(applicant_id=applicant)
        return queryset


class EmpoyerFeedBacksViewSet(ListRetrieveViewSet):
    """Просмотр откликов от соискателей"""

    serializer_class = ShowFeedbacksSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        user = self.request.user
        employer = get_object_or_404(Employer, user_id=user.id)
        queryset = Feedback.objects.all().filter(vacancy__company=employer)
        return queryset


class ExperienceViewSet(ModelViewSet):
    """Опыт работы"""

    serializer_class = ShowExperienceSerializer
    permission_classes = [IsApplicant]

    def get_queryset(self):
        user = self.request.user
        applicant = get_object_or_404(Applicant, user_id=user.id)
        queryset = Experience.objects.all().filter(applicant_id=applicant)
        return queryset
