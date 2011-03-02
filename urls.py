from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^', include('hark.harkweb.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^shared/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': '/var/www/hark/shared'
        }),
    )
