from hark.harkweb.models import Artist, Album, Song
from django.contrib import admin

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]

admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)


