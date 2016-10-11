# -*- coding: utf-8 -*-

from django.conf.urls import url
from mptt_graph.views import ModelListGraphsView, ModelGraphView


urlpatterns = [
    url(r'^(?P<modpath>[-._\w]+)/(?P<pk>[0-9]+)/$', ModelGraphView.as_view(), name="mpttgraph-detail"),
    url(r'^', ModelListGraphsView.as_view(), name="mpttgraph-index"),
]
