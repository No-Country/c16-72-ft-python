def user_groups_context(request):
    user = request.user
    return {
        'is_medical': user.groups.filter(name='Medicals').exists() or user.is_staff,
        'is_patient': user.groups.filter(name='Patients').exists(),
    }

