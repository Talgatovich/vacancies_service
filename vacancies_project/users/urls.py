from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/log_in.html'),
        name='login'
    ),
    path('employer-signup/', views.employer_registration, name='employer-signup'),
    path('applicant-signup/', views.applicant_registration, name='applicant-signup'),
]
