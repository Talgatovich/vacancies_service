from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.models import Applicant, Employer

from .forms import ApplicantCreationForm, CreationForm, EmployerCreationForm

User = get_user_model()


def employer_registration(request):
    userform = CreationForm(request.POST)
    form = EmployerCreationForm(request.POST)

    if request.method == "POST":
        if form.is_valid() and userform.is_valid():
            username = userform.cleaned_data["username"]
            email = form.cleaned_data["email"]
            company_name = form.cleaned_data["company_name"]
            staff_quantity = form.cleaned_data["staff_quantity"]
            city = form.cleaned_data["city"]
            address = form.cleaned_data["address"]
            phone_number = form.cleaned_data["phone_number"]
            tg_link = form.cleaned_data["tg_link"]
            vk_link = form.cleaned_data["vk_link"]
            about = form.cleaned_data["about"]

            userform.save()
            user = User.objects.get(username=username)
            form.cleaned_data["user"] = user
            Employer.objects.create(**form.cleaned_data)
            return redirect(reverse("vacancies:index"))
        context = {"form": form, "userform": userform}
        return render(request, "users/employer-signup.html", context=context)

    context = {"form": form, "userform": userform}
    return render(request, "users/employer-signup.html", context=context)


def applicant_registration(request):
    userform = CreationForm(request.POST)
    form = ApplicantCreationForm(request.POST)

    if request.method == "POST":
        if form.is_valid() and userform.is_valid():
            username = userform.cleaned_data["username"]
            email = form.cleaned_data["email"]
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            patronymic = form.cleaned_data["patronymic"]
            city = form.cleaned_data["city"]
            address = form.cleaned_data["address"]
            phone_number = form.cleaned_data["phone_number"]
            tg_link = form.cleaned_data["tg_link"]
            vk_link = form.cleaned_data["vk_link"]
            userform.save()
            user = User.objects.get(username=username)
            form.cleaned_data["user"] = user
            Applicant.objects.create(**form.cleaned_data)
            return redirect(reverse("vacancies:index"))
        context = {"form": form, "userform": userform}
        return render(request, "users/applicant-signup.html", context=context)

    context = {"form": form, "userform": userform}
    return render(request, "users/applicant-signup.html", context=context)
