from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from accounts.models import Applicant, Employer
from vacancies.models import Feedback, Vacancy

from .forms import VacancyCreationForm
from .utils import get_is_applicant

User = get_user_model()


def index(request):
    """Все вакансии"""
    is_applicant = get_is_applicant(request, Applicant)
    template = "index.html"
    vacancies = Vacancy.objects.all().select_related("company").order_by("-id")
    context = {"vacancies": vacancies, "is_applicant": is_applicant}
    return render(request, template, context=context)


def vacancy_detail(request, pk):
    """Детальная информация о вакансии"""
    is_applicant = False
    try:
        applicant = Applicant.objects.get(user_id=request.user.id)
        is_applicant = True
    except Exception:
        applicant = None
    vacancy = Vacancy.objects.select_related("company").get(pk=pk)
    is_sent = Feedback.objects.filter(vacancy=vacancy, applicant=applicant).exists
    template = "vacancy_detail.html"

    context = {
        "vacancy": vacancy,
        "is_applicant": is_applicant,
        "is_sent": is_sent,
    }
    return render(request, template, context=context)


def send_feedback(request, pk):
    """Отправка отклика"""
    is_applicant = get_is_applicant(request, Applicant)
    template = reverse("vacancies:vacancy_detail", args=((pk,)))
    if is_applicant:
        applicant = get_object_or_404(Applicant, user_id=request.user.id)
        vacancy = get_object_or_404(Vacancy, pk=pk)
        Feedback.objects.create(vacancy=vacancy, applicant=applicant)
    return redirect(template)


def feedback_list(request):
    """Отклики соискателя"""
    template = "applicant_feedback.html"
    is_applicant = get_is_applicant(request, Applicant)
    applicant = get_object_or_404(Applicant, user_id=request.user.id)
    feedbacks = applicant.feedback.all().prefetch_related(
        "vacancy",
    ).prefetch_related("vacancy__company").order_by("-id")
    context = {
        "feedbacks": feedbacks,
        "is_applicant": is_applicant,
    }
    return render(request, template, context=context)


def del_applicant_feedback(request, pk):
    """Удаление отклика соискателя"""
    applicant = get_object_or_404(Applicant, user_id=request.user.id)
    feedback = get_object_or_404(Feedback, pk=pk)
    if feedback.applicant != applicant:
        return redirect('vacancies:index')
    feedback.delete()
    return redirect('vacancies:applicant_feedback')


def employer_feedback_list(request):
    """Отклики от соискателей"""
    template = "employer_feedback.html"
    is_applicant = get_is_applicant(request, Applicant)
    employer = get_object_or_404(Employer, user_id=request.user.id)
    feedbacks = (
        Feedback.objects.all()
        .select_related("applicant")
        .filter(vacancy__company=employer)
        .order_by("-id")
    )
    context = {
        "feedbacks": feedbacks,
        "is_applicant": is_applicant,
    }
    return render(request, template, context=context)


def create_vacancy(request):
    """Создание вакансии"""
    is_applicant = get_is_applicant(request, Applicant)
    form = VacancyCreationForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        company = Employer.objects.get(user=request.user)
        if form.is_valid():
            title = form.cleaned_data["title"]
            salary = form.cleaned_data["salary"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]

            new_vacancy = form.save(commit=False)
            new_vacancy.company = company
            new_vacancy.save()
            return redirect(reverse("vacancies:index"))
        context = {
            "form": form,
            "is_applicant": is_applicant,
        }
        return render(request, "create_vacancy.html", context=context)

    context = {
        "form": form,
        "is_applicant": is_applicant,
    }
    return render(request, "create_vacancy.html", context=context)
