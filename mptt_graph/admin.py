# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt_graph.models import GraphModel


@admin.register(GraphModel)
class UrlTreeAdmin(admin.ModelAdmin):
    list_display = ["title", "model_path", "model_pk"]
