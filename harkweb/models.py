import re
import urllib
from django.db import models
from hark.harkweb.templatetags.harkweb_extras import harkify

class Artist(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist)
    songregex = models.CharField(max_length=128)

    def __unicode__(self):
        return self.fullname()

    def fullname(self):
        return '%s - %s' % (self.artist, self.name)

    def urlpath(self):
        return '%s/%s/' % (harkify(self.artist), harkify(self.name))

    def songs_sorted_by_track(self):
        return self.song_set.all().order_by('track')

class Song(models.Model):
    name = models.CharField(max_length=64)
    album = models.ForeignKey(Album)
    track = models.IntegerField()

    def __unicode__(self):
        return self.name

    def urlname(self):
        urlname = re.sub(
            r'(\(\?P<track>.*?\))', '%02d' % (self.track),
            self.album.songregex
        )
        urlname = re.sub(r'\\(.)', r'\1', urlname)
        urlname = re.sub(r'(\(\?P<name>.*?\))', self.name, urlname)
        urlname = urllib.quote(urlname.encode('utf-8'))
        return urlname
