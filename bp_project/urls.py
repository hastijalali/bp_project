from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import application
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('application/', include('application.urls', namespace='application')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
