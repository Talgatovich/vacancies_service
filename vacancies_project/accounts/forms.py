from django import forms

from .models import Experience


class ExperienceCreationForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ("applicant",)
