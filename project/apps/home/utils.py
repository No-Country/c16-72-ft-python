from django.contrib.auth.models import Group
from studies_medicals.models import TypeStudieMedical

def check_and_create_groups_and_models():
    try:
        Group.objects.get_or_create(name='Medicals')
        Group.objects.get_or_create(name='Patients')
    except:
        pass

    type_names = [
        "Exámenes de laboratorio",
        "Examen físico",
        "Pruebas de diagnóstico por imagen",
        "Pruebas de función pulmonar",
        "Pruebas de función cardíaca",
        "Pruebas de función renal",
        "Pruebas de función hepática",
        "Pruebas de densidad ósea"
    ]
    for name in type_names:
        try:
            TypeStudieMedical.objects.get_or_create(name=name)
        except:
            pass