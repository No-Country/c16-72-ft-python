#Funcion para determinar rol del usuario
def get_rol_user(user, group):
    if user.groups.filter(name=group).exists():
        return True
    
#Funcion para traer tipos de estudios de cierto usuario y que no se repitan
def get_types_studies_user(studies_medicals):
    type_studies = []
    seen_studies = {}
            
    for study in studies_medicals:
        study.type_studie.date = study.date_joined
        study.type_studie.patient = study.patient
        if study.type_studie.id not in seen_studies:
            type_studies.append(study.type_studie)
            seen_studies[study.type_studie.id] = study.type_studie
    
    return type_studies

#funcion para no tener usuarios de cierto estudios duplicados
def get_users_studies_medicals(studies_medicals):
    user_studies_medicals = []
    seen_users_studies_medicals = {}
    
    for studie_medical in studies_medicals:
        if studie_medical.patient.id not in seen_users_studies_medicals:
            user_studies_medicals.append(studie_medical)
            seen_users_studies_medicals[studie_medical.patient.id] = studie_medical.patient
    
    return user_studies_medicals


def validate_image_extension(filename):    
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        return True
    else:
        return False