# Django mptt graph

Graphical representation of any mptt model.

## Install

Clone, make migrations and migrate

Add `"mptt_graph",` to installed apps.

Urls: `url('^graph/', include('mptt_graph.urls')),`

## Usage

1. Graph from a tree

Go to the admin and make a Graph model object:

In `Model path` put the path to the model: `myapp.models.MyModel`

In `Root node primary key` put the primary key of the node you wish to start from

Go to `/graph/`

2. Graph directly from an url

Example: `/graph/myapp.models.MyModel/1/`

First url parameter is the path to the model and second is the model primary key

3. Graph from custom queries

Make a view that sends a `nodes` context variable to `/templates/mptt_graph/tree.html`

## Screenshot

 ![Tree screenshot](https://raw.githubusercontent.com/synw/django-mptt_graph/master/doc/img/screenshot.png)