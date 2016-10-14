# Django mptt graph

Graphical representation of any mptt model.

## Install

Clone, add `"mptt_graph",` to installed apps, make migrations and migrate

Urls: `url('^graph/', include('mptt_graph.urls')),`

## Usage

#### Graph from a tree

Go to the admin and make a Graph model object:

In `Model path` put the path to the model: `myapp.models.MyModel`

In `Root node primary key` put the primary key of the node you wish to start from

Go to `/graph/`

#### Graph directly from an url

Example: `/graph/myapp.models.MyModel/1/`

First url parameter is the path to the model and second is the root node primary key

#### Graph from custom queries

Make a view that sends a `nodes` context variable to `/templates/mptt_graph/tree.html` or use the inline template:
``{% include "mptt_graph/tree_inline.html" %}``

## Screenshot

 ![Tree screenshot](https://raw.githubusercontent.com/synw/django-mptt-graph/master/doc/img/screenshot.png)