from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "vacancies"

urlpatterns = [
    path("vacancies/", views.index, name="index"),
    path("vacancies/<int:pk>/", views.vacancy_detail, name="vacancy_detail"),
    path("vacancies/<int:pk>/feedback/", views.send_feedback, name="feedback"),
    path("apl-feedback/", views.feedback_list, name="applicant_feedback"),
    path("empl-feedback/", views.employer_feedback_list, name="employer_feedback"),
    path("create-vacancy/", views.create_vacancy, name="create_vacancy"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
