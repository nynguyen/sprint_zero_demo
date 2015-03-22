from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = patterns('',
	(r'^filesAndForms/', include('filesAndForms.urls')),
	(r'^$', RedirectView.as_view(url='filesAndForms/list/')),	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
