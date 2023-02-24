from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "vacancies"

urlpatterns = [

    path('vacancies/', views.index, name="index"),
    path('vacancies/<int:pk>/', views.vacancy_detail, name="vacancy_detail"),
]
urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
