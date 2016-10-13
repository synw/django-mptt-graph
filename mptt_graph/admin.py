# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt_graph.models import GraphModel, TreeNode


@admin.register(GraphModel)
class UrlTreeAdmin(admin.ModelAdmin):
    list_display = ["title", "model_path", "model_pk"]


@admin.register(TreeNode)
class TreeNodeAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
