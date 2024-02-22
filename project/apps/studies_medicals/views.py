from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse

from .models import StudiesMedicals
from users.models import User
from .forms import StudieMedicalForm
from medical_history.models import MedicalHistory
from .utils import render_to_pdf

# Create your views here.

class ListStudiesMedicalsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        
        if request.user.groups.filter(name='Medicals').exists():
            studies_medicals = StudiesMedicals.objects.filter(medical=request.user)
            
            if studies_medicals:
                context['studies_medicals'] = studies_medicals
            else:
                messages.success(self.request, "Aun no tines examnes medicos asosciados", extra_tags="alert alert-danger")

            return render(request, 'studies_medicals/medical/list.html', context)
        
        if request.user.groups.filter(name='Patients').exists():
            try:
                medical_history = MedicalHistory.objects.get(patient=request.user)
                studies_patients = StudiesMedicals.objects.filter(patient=medical_history)  
                context['studies_patients'] = studies_patients
            except:
                messages.success(self.request, "Aun no tines examenes medicos asosciados", extra_tags="alert alert-danger")
                
            return render(request, 'studies_medicals/patient/list.html', context)
        
        else:
            return render(request, 'components/404.html')

class StudieMedicalPatientPDF(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.groups.filter(name='Patients').exists():
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
        
        if request.user.groups.filter(name='Medicals').exists():
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                context['studie_medical'] = studie_medical
                return render(request, 'studies_medicals/medical/detail.html', context)
            except:
                return render(request, 'components/404.html')
        
        else:
            return render(request, 'components/404.html')
             
class CreateStudieMedical(View):
    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Medicals').exists():  
            form = StudieMedicalForm()
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/create.html', context)

        else:
            return render(request, 'components/404.html')
        
    def post(self, request, *args, **kwargs):   
        if request.user.groups.filter(name='Medicals').exists():     
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
                    return redirect('medical_history:index')
                
                except User.DoesNotExist:
                    messages.success(request, "El dni del paciente no existe", extra_tags="alert alert-danger")
                except MedicalHistory.DoesNotExist:
                    messages.success(request, "El paciente no tiene un hisroial medico asociado", extra_tags="alert alert-danger")
              
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/create.html', context)
        
        else: 
            return render(request, 'components/404.html')

class UpdateStudieMedical(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.groups.filter(name='Medicals').exists():
            try:
                studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
                medical_history = studie_medical.patient
                form = StudieMedicalForm(instance=studie_medical, initial={'dni_patient' : medical_history.patient})
                context = {'form' : form}
                return render(request, 'studies_medicals/medical/update.html', context)
            except:
                return render(request, 'components/404.html')
        
        else:
            return render(request, 'components/404.html')
        
    def post(self, request, pk, *args, **kwargs):   
        if request.user.groups.filter(name='Medicals').exists():     
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
                    return redirect('studies_medicals:studiesmedicals_detail', pk=pk)
                
                except User.DoesNotExist:
                    messages.success(request, "El dni del paciente no existe", extra_tags="alert alert-danger")
                except MedicalHistory.DoesNotExist:
                    messages.success(request, "El paciente no tiene un hisroial medico asociado", extra_tags="alert alert-danger")
              
            context = {'form' : form}
            return render(request, 'studies_medicals/medical/update.html', context)
        
        else: 
            return render(request, 'components/404.html')

def delete_studieMedical_view(request, pk):
    if request.user.groups.filter(name='Medicals').exists():
        studie_medical = get_object_or_404(StudiesMedicals, pk=pk)
        studie_medical.delete()
        messages.success(request, "El estudio medico se ha eliminado", extra_tags="alert alert-success")
        return redirect('studies_medicals:studiesmedicals_list')
    else:
        return render(request, 'components/404.html')