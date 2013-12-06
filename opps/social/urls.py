#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from piston.resource import Resource

from opps.api import ApiKeyAuthentication

from .api import LikedHandler, FavoritedHandler


auth = ApiKeyAuthentication()
liked_resource = Resource(handler=LikedHandler)
favorited_resource = Resource(handler=FavoritedHandler, authentication=auth)

urlpatterns = patterns(
    '',
    url(r'^api/social/liked/$', liked_resource),
    url(r'^api/social/favorited/$', favorited_resource),
)
