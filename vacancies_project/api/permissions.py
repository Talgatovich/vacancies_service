from rest_framework import permissions

from accounts.models import Applicant, Employer


class IsEmployerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.company_id == request.user.id
            or request.method in permissions.SAFE_METHODS
        )


class IsEmployer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        employer = Employer.objects.filter(user_id=user.id)
        return request.user.is_authenticated and employer.exists()


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        applicant = Applicant.objects.filter(user_id=user.id)
        return request.user.is_authenticated and applicant.exists()

    def has_object_permission(self, request, view, obj):
        applicant = Applicant.objects.get(user_id=request.user.id)
        return obj.applicant == applicant
