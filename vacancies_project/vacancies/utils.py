def get_is_applicant(request, model):
    if request.user.is_authenticated:
        return model.objects.filter(user_id=request.user.id).exists()
    return False
