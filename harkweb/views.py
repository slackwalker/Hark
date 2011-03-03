from django.http import Http404
from django.views.generic import list_detail
from hark.harkweb.models import Artist, Album

def albums_by_artist(request, artistname):
    artistname = artistname.replace('_', ' ')
    try:
        artist = Artist.objects.get(name__iexact=artistname)
    except Artist.DoesNotExist:
        raise Http404

    return list_detail.object_list(
        request,
        queryset = Album.objects.filter(artist = artist),
        template_object_name = 'album',
        extra_context = { 'artist' : artist },
    )

def album_detail(request, artistname, albumname):
    artistname = artistname.replace('_', ' ')
    try:
        artist = Artist.objects.get(name__iexact = artistname)
    except Artist.DoesNotExist:
        raise Http404

    albumname = albumname.replace('_', ' ')
    try:
        album = Album.objects.get(
            name__iexact = albumname,
            artist = artist
        )
    except Album.DoesNotExist:
        raise Http404

    return list_detail.object_detail(
        request,
        queryset = Album.objects.all(),
        template_object_name = 'album',
        object_id = album.id,
    )

