from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VacancyAPIView,
    VacancyDetail,
    EmployerRegistration,
    ApplicantRegistration,
    VacancyViewSet,
    SendFeedBackViewSet,
    ApplicantFeedBacksViewSet,
    EmpoyerFeedBacksViewSet,
)

router = DefaultRouter()
app_name = "api"
router.register("vacancies", VacancyViewSet, basename="vacancies")
router.register(r"vacancies/(?P<vacancy_id>\d+)/feedback", SendFeedBackViewSet, basename="feedback")
router.register("applicant-feed", ApplicantFeedBacksViewSet, basename="applicant_feedback")
router.register("employer-feed", EmpoyerFeedBacksViewSet, basename="employer_feedback")


urlpatterns = [
    path('', include(router.urls)),
    path('reg_employer/', EmployerRegistration.as_view()),
    path('reg_applicant/', ApplicantRegistration.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('vacancies/<int:pk>/feedback/', SendFeedBackView.as_view()),
    # path('vacancies/', VacancyAPIView.as_view(),  name="vacancies"),
    # path("vacancies/<int:pk>/", VacancyDetail.as_view(), name="vacancy_detail"),
]