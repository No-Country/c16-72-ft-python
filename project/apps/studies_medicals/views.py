from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .models import StudiesMedicals, TypeStudieMedical
from users.models import User
from .forms import StudieMedicalForm
from medical_history.models import MedicalHistory
from .utils import render_to_pdf, get_rol_user, get_types_studies_user, get_users_studies_medicals

# Create your views here.

class ListTypeStudieMedical(View):
    def get(self, request, pk=None, *args, **kwargs):
        if get_rol_user(request.user, 'Medicals'):
            patient = StudiesMedicals.objects.filter(patient=pk, medical=request.user).first()
            studies_medicals = StudiesMedicals.objects.filter(medical=request.user, patient__id=pk).select_related('type_studie')
            
            types_studies = get_types_studies_user(studies_medicals)
         
            return render(request, 'studies_medicals/types/list.html', {'types_studies' : types_studies, 'patient' : patient})
    
        
        if get_rol_user(request.user, 'Patients'):
            studies_medicals = StudiesMedicals.objects.filter(patient__patient=request.user).select_related('type_studie')
            
            type_studies = get_types_studies_user(studies_medicals)
            
            return render(request, 'studies_medicals/types/list.html', {'types_studies' : type_studies})

class ListStudiesMedicalsInTypesView(View):
    def get(self, request, pk_patient=None, pk_type=None, *args, **kwargs):
        context = {}
        
        if get_rol_user(request.user, 'Medicals'):
            patient = StudiesMedicals.objects.filter(patient=pk_patient, medical=request.user, type_studie=pk_type).first()
            type_studie = StudiesMedicals.objects.filter(type_studie=pk_type, medical=request.user, patient=pk_patient).first()
            studies_medicals = StudiesMedicals.objects.filter(medical=request.user, type_studie=pk_type, patient=pk_patient)
            
            context['studies_medicals'] = studies_medicals
            
            context['type_studie'] = type_studie
            context['patient'] = patient

            return render(request, 'studies_medicals/medical/list_types.html', context)
        
        if get_rol_user(request.user, 'Patients'):
            type_studie = StudiesMedicals.objects.filter(type_studie=pk_type, patient__patient=request.user).first()
            studies_medicals = StudiesMedicals.objects.filter(patient__patient=request.user, type_studie=pk_type)
            
            context['studies_medicals'] = studies_medicals
            
            context['type_studie'] = type_studie

            return render(request, 'studies_medicals/patient/list_types.html', context)
        
        else:
            return render(request, 'components/404.html')

class ListStudiesMedicalsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        consult = request.GET.get("consult")
        
        if get_rol_user(request.user, 'Medicals'):
            studies_medicals = StudiesMedicals.objects.filter(medical=request.user)
            
            if studies_medicals:
                if consult:
                    
                    studies_medicals = StudiesMedicals.objects.filter(
                        Q(patient__patient__dni__icontains=consult) | Q(patient__patient__name__icontains=consult) | Q(patient__patient__last_name__icontains=consult), medical=request.user
                    )
                    
                    users_studies_medicals = get_users_studies_medicals(studies_medicals)
                    context['studies_medicals'] = users_studies_medicals
                else:
                    
                    users_studies_medicals = get_users_studies_medicals(studies_medicals)
                    context['studies_medicals'] = users_studies_medicals

            return render(request, 'studies_medicals/medical/list.html', context)
        
        else:
            return render(request, 'components/404.html')

class StudieMedicalPatientPDF(View):
    def get(self, request, pk, *args, **kwargs):
        if get_rol_user(request.user, 'Patients'):
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                context = {'studie_medical': studie_medical}
                pdf = render_to_pdf('studies_medicals/patient/studie_medical_pdf_patient.html', context)
                if pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    filename = f'estudio_medico_{studie_medical.pk}.pdf'
                    content = f'attachment; filename="{filename}"'
                    response['Content-Disposition'] = content
                    return response
                else:
                    return HttpResponse("Error al generar el PDF", status=500)
            except Exception as e:
                return render(request, 'components/404.html')
        else:
            return render(request, 'components/404.html')

class DetailStudieMedicalView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        
        if get_rol_user(request.user, 'Medicals'):
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                context['studie_medical'] = studie_medical
                return render(request, 'studies_medicals/medical/detail.html', context)
            except:
                return render(request, 'components/404.html')
        
        if get_rol_user(request.user, 'Patients'):
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                context['studie_medical'] = studie_medical
                return render(request, 'studies_medicals/patient/detail.html', context)
            except:
                return render(request, 'components/404.html')
        
        else:
            return render(request, 'components/404.html')
             
class CreateStudieMedical(View):
    def get(self, request, *args, **kwargs):
        if get_rol_user(request.user, 'Medicals'):  
            form = StudieMedicalForm()
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/form.html', context)

        else:
            return render(request, 'components/404.html')
        
    def post(self, request, *args, **kwargs):   
        if get_rol_user(request.user, 'Medicals'):     
            if request.method == "POST":
                form = StudieMedicalForm(request.POST or None,  request.FILES)
            if form.is_valid():
                
                dni_patient = form.cleaned_data.get('dni_patient')
    
                try:
                    patient = User.objects.get(dni=int(dni_patient))
                    medical_history = MedicalHistory.objects.get(patient=patient)
                    
                    new_studie = form.save(commit=False)
                    new_studie.medical = request.user
                    new_studie.patient = medical_history
                    new_studie.save()
                    
                    messages.success(request, "El estudio medico se a creado", extra_tags="alert alert-success")
                    return redirect('studies_medicals:studiesmedicals_list')
                
                except User.DoesNotExist:
                    messages.success(request, "El dni del paciente no existe", extra_tags="alert alert-danger")
                except MedicalHistory.DoesNotExist:
                    messages.success(request, "El paciente no tiene un historial medico asociado", extra_tags="alert alert-danger")
              
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/form.html', context)
        
        else: 
            return render(request, 'components/404.html')

class UpdateStudieMedical(View):
    def get(self, request, pk, *args, **kwargs):
        if get_rol_user(request.user, 'Medicals'):
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                medical_history = studie_medical.patient
                form = StudieMedicalForm(instance=studie_medical, initial={'dni_patient' : medical_history.patient})
                context = {'form' : form}
                return render(request, 'studies_medicals/medical/form.html', context)
            except:
                return render(request, 'components/404.html')
        
        else:
            return render(request, 'components/404.html')
        
    def post(self, request, pk, *args, **kwargs):   
        if get_rol_user(request.user, 'Medicals'):  
            if request.method == "POST":
                try:
                    studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                    medical_history = studie_medical.patient
                    form = StudieMedicalForm(request.POST or None, request.FILES, instance=studie_medical, initial={'dni_patient' : medical_history.patient})
                except:
                    return render(request, 'components/404.html')
                
            if form.is_valid():
                
                dni_patient = form.cleaned_data.get('dni_patient')
    
                try:
                    patient = User.objects.get(dni=int(dni_patient))
                    medical_history = MedicalHistory.objects.get(patient=patient)
                    
                    update_studie = form.save(commit=False)
                    update_studie.medical = request.user
                    update_studie.patient = medical_history
                    update_studie.save()
                    messages.success(request, "El estudio medico se ha actualizado", extra_tags="alert alert-success")
                    return redirect('studies_medicals:studiesmedicals_list')
                
                except User.DoesNotExist:
                    messages.success(request, "El dni del paciente no existe", extra_tags="alert alert-danger")
                except MedicalHistory.DoesNotExist:
                    messages.success(request, "El paciente no tiene un historial medico asociado", extra_tags="alert alert-danger")
              
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/form.html', context)
        
        else: 
            return render(request, 'components/404.html')

def delete_studieMedical_view(request, pk):
    if get_rol_user(request.user, 'Medicals'):
        studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
        studie_medical.delete()
        messages.success(request, "El estudio medico se ha eliminado", extra_tags="alert alert-success")
        return redirect('studies_medicals:studiesmedicals_list')
    else:
        return render(request, 'components/404.html')