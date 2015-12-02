#!/usr/bin/python
# vim: set fileencoding=utf8 :

from django.db import models
from sorl.thumbnail import get_thumbnail

class Type(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Theme(models.Model):
    type = models.ForeignKey(Type, related_name='themes')
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()
    rendering = models.ImageField(upload_to='theme/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def rendering_url(self):
        im = get_thumbnail(self.rendering, 'x100')
        return '<img src="%s" height=%s>' % (im.url, im.y)

    rendering_url.allow_tags = True

class Template(models.Model):
    theme = models.ForeignKey(Theme, related_name='templates')
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
