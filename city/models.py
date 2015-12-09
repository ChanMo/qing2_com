#!/usr/bin/python
# vim: set fileencoding=utf8 :

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class City(MPTTModel):
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def tree_name(self, parent=False):
        address = ''
        for item in self.get_ancestors():
            if parent:
                address += item.name + ','
            else:
                address += '---'
        address += ' ' + self.name
        return address

    class MPTTMeta:
        order_insertion_by = ['name']
