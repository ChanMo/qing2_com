#!/usr/bin/python
# vim: set fileencoding=utf8 :

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey

from theme.models import Theme, Template

class Site(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='sites')
    slug = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, related_name='sites')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Page(MPTTModel):
    site = models.ForeignKey(Site, related_name='pages')
    title = models.CharField(max_length=200)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='site/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    template = models.ForeignKey(Template, related_name='pages')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sort = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta(object):
        ordering = ['sort']

    def image_url(self):
        if self.image:
            im = get_thumbnail(self.image, '50x50', crop='center')
            return '<img src=%s height="%s">' % (im.url, im.y)
        else:
            return ''

    image_url.allow_tags = True
