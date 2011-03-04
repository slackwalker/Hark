from django.db import models
from hark.harkweb.templatetags.harkweb_extras import harkify

class Artist(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.fullname()

    def fullname(self):
        return '%s - %s' % (self.artist, self.name)

    def urlpath(self):
        return '%s/%s/' % (harkify(self.artist), harkify(self.name))
        

class Song(models.Model):
    name = models.CharField(max_length=64)
    album = models.ForeignKey(Album)
    track = models.IntegerField()

    def __unicode__(self):
        return self.name

    def urlname(self):
        return '%02d_%s' % (self.track, harkify(self.name))

