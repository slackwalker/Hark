from hark.harkweb.models import Artist, Album, Song
from django.contrib import admin
import os
import re
import glob
from django.db.models.signals import post_save
from hark import settings

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]

admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)

def update_songs_for_album(sender, instance, **kwargs):
    albumpath = settings.MEDIA_ROOT + 'albums' + os.sep + instance.urlpath() \
        + 'mp3' + os.sep + '*.mp3'
    songlist = glob.glob(albumpath)
        
    for songpath in songlist:
        # get just the filename minus the extension
        songfile = os.path.basename(songpath)[:-4] 
        songmatch = re.match(instance.songregex, songfile)
        try:
            curr_song = instance.song_set.get(track = songmatch.group('track'))
        except:
            newsong = Song(
                album = instance,
                track = songmatch.group('track'),
                name = songmatch.group('name'),
            )
            newsong.save()

post_save.connect(update_songs_for_album, sender=Album)

