from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VacancyAPIView, VacancyDetail

router = DefaultRouter()
app_name = "api"
# router.register('vacancies', VacancyViewSet, basename='vacancies/')


urlpatterns = [
    path('', include(router.urls)),
    path('vacancies/', VacancyAPIView.as_view(),  name="vacancies"),
    path("vacancies/<int:pk>/", VacancyDetail.as_view(), name="vacancy_detail"),
]