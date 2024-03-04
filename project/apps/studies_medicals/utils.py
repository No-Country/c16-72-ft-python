from django.template.loader import get_template
from django.http import HttpResponse

from io import BytesIO
from xhtml2pdf import pisa

#Funcion para pasar una plantilla django a pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        return response
    
    return None

#Funcion para determinar rol del usuario
def get_rol_user(user, group):
    if user.groups.filter(name=group).exists():
        return True
    
#Funcion para traer tipos de estudios de cierto usuario
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