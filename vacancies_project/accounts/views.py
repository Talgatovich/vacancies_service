from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from vacancies.utils import get_is_applicant

from .forms import ExperienceCreationForm
from .models import Applicant, Experience


@login_required
def profile(request, pk):
    template = "profile.html"
    is_applicant = get_is_applicant(request, Applicant)
    applicant = Applicant.objects.get(pk=pk)
    experiences = applicant.experience.all().order_by("pk")
    context = {
        "experiences": experiences,
        "is_applicant": is_applicant,
        "applicant": applicant,
    }
    return render(request, template, context=context)


@login_required
def applicant_profile(request):
    template = "applicant_profile.html"
    is_applicant = get_is_applicant(request, Applicant)
    try:
        applicant = Applicant.objects.get(user_id=request.user.id)
        experiences = applicant.experience.all()
    except Exception:
        return render(request, template, {"is_applicant": is_applicant})
    context = {
        "experiences": experiences,
        "is_applicant": is_applicant,
        "applicant": applicant,
    }
    return render(request, template, context=context)


def add_experience(request):
    is_applicant = get_is_applicant(request, Applicant)
    form = ExperienceCreationForm(
        request.POST or None,
    )

    if request.method == "POST":
        applicant = Applicant.objects.get(user_id=request.user.id)
        if form.is_valid():
            company_name = form.cleaned_data["company_name"]
            start_date = form.cleaned_data["start_date"]
            finish_date = form.cleaned_data["finish_date"]
            job_results = form.cleaned_data["job_results"]

            new_experience = form.save(commit=False)
            new_experience.applicant = applicant
            new_experience.save()
            return redirect(reverse("accounts:applicant_profile"))
        context = {
            "form": form,
            "is_applicant": is_applicant,
        }
        return render(request, "create_experience.html", context=context)

    context = {
        "form": form,
        "is_applicant": is_applicant,
    }
    return render(request, "create_experience.html", context=context)


@login_required
def experience_edit(request, pk):
    is_applicant = get_is_applicant(request, Applicant)
    edit_experience = get_object_or_404(Experience, pk=pk)
    applicant = Applicant.objects.get(user_id=request.user.id)
    if applicant != edit_experience.applicant:
        return redirect('vacancies:index', )
    form = ExperienceCreationForm(
        request.POST or None,
        instance=edit_experience
    )
    if form.is_valid():
        experience = form.save(commit=False)
        experience.applicant = applicant
        experience.save()
        return redirect('accounts:applicant_profile')
    context = {
        "form": form,
        "is_applicant": is_applicant,
    }
    return render(request, 'create_experience.html', context)


@login_required
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    applicant = Applicant.objects.get(user_id=request.user.id)
    if applicant != experience.applicant:
        return redirect('vacancies:index')
    experience.delete()
    return redirect('accounts:applicant_profile')

