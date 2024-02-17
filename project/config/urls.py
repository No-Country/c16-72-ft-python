from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'))),
<<<<<<< HEAD
    path('users/', include(('users.urls', 'users'))),
    path('clinic/', include(('medical_history.urls', 'medical_history'))),
    path('clinic/studies/', include(('studies_medicals.urls', 'studies_medicals')))
=======
    path('clinica/', include(('historias_clinicas.urls', 'historias_clinicas')))
>>>>>>> f52097cce55783dc35dcd98d0212a8909538b403
]

# Valido en entorno de desarrollo: DEBUG= True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()