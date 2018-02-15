# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel


class GraphModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_(u"Title"))
    model_path = models.CharField(max_length=200, verbose_name=_(u"Model path"),
                                  help_text=_(u"Path to the model: ex: "
                                              "myapp.models.MyModel"))
    model_pk = models.PositiveSmallIntegerField(
        verbose_name=_(u"Root node primary key"))

    class Meta:
        verbose_name = _(u'Mptt graph')
        verbose_name_plural = _(u'Mptt graphs')
        ordering = ('title',)

    def __str__(self):
        return self.title


class TreeNode(MPTTModel):
    title = models.CharField(max_length=200, verbose_name=_(u"Title"))
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children',
                            verbose_name=_(u'Parent node'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _(u'Tree node')
        verbose_name_plural = _(u'Tree nodes')
        ordering = ('title',)

    def __str__(self):
        return self.title
