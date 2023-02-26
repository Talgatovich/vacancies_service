from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from accounts.models import Applicant, Employer

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', )


class EmployerCreationForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ('user',)


class ApplicantCreationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('user',)