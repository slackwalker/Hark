from django.db import models

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

class Song(models.Model):
    name = models.CharField(max_length=64)
    filename = models.CharField(max_length=64)
    album = models.ForeignKey(Album)
    track = models.IntegerField()

    def __unicode__(self):
        return self.name

