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