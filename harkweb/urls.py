from django.conf.urls.defaults import *
from django.views.generic import list_detail
from hark.harkweb.views import albums_by_artist, album_detail

from hark.harkweb.models import Album

album_info = {
    'queryset': Album.objects.all(),
    'template_object_name': 'album',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, album_info),
    (r'^([\w]+)/$', albums_by_artist),
    (r'^([\w]+)/([\w]+)/$', album_detail),
)
