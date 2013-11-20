#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Count
from tastypie.constants import ALL
from tastypie.resources import ModelResource

from opps.api import MetaBase, ApiAuthentication

from .models import Liked as LikedModel
from .models import Favorited as FavoritedModel


class Liked(ModelResource):
    class Meta:
        allowed_methods = ['get', 'post']
        filtering = {
            'path': ALL,
            'user': ALL,
        }
        queryset = LikedModel.objects.all()
        include_resource_uri = False
        excludes = ['point', 'id']
        authentication = ApiAuthentication(['post'])

    #def get_object_list(self, request):
    #    return super(Liked, self).get_object_list(request).values('path').annotate(p=Count('path'))

    def dehydrate(self, bundle):
        bundle.data['like'] = LikedModel.objects.get_like(bundle.data['path'])
        bundle.data['dislike'] = LikedModel.objects.get_dislike(
            bundle.data['path'])
        bundle.data['total'] = LikedModel.objects.get_total(
            bundle.data['path'])
        return bundle


class Favorited(ModelResource):
    class Meta:
        allowed_methods = ['get', 'post']
        filtering = {
            'path': ALL,
            'user': ALL,
        }
        queryset = FavoritedModel.objects.all()
        include_resource_uri = False
        authentication = ApiAuthentication()
