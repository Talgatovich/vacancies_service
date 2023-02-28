from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ApplicantFeedBacksViewSet,
    ApplicantRegistration,
    EmployerRegistration,
    EmpoyerFeedBacksViewSet,
    ExperienceViewSet,
    SendFeedBackViewSet,
    VacancyViewSet,
)

router = DefaultRouter()

router.register("vacancies", VacancyViewSet, basename="vacancies")
router.register(
    r"vacancies/(?P<vacancy_id>\d+)/feedback", SendFeedBackViewSet, basename="feedback"
)
router.register(
    "applicant-feed", ApplicantFeedBacksViewSet, basename="applicant_feedback"
)
router.register("employer-feed", EmpoyerFeedBacksViewSet, basename="employer_feedback")
router.register("experience", ExperienceViewSet, basename="experience")

urlpatterns = [
    path("", include(router.urls)),
    path("reg_employer/", EmployerRegistration.as_view()),
    path("reg_applicant/", ApplicantRegistration.as_view()),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
