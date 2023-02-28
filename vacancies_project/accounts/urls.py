from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("applicant-profile/", views.applicant_profile, name="applicant_profile"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("add-experience/", views.add_experience, name="add_experience"),
]
