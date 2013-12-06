#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.contrib.auth import get_user_model

from opps.api import BaseHandler

from .models import Liked, Favorited


class Handler(BaseHandler):
    allowed_methods = ['GET', 'POST']


class LikedHandler(Handler):
    model = Liked
    excludes = ['point', 'id']

    def read(self, request):
        base = self.model.objects
        if request.GET.items():
            method = getattr(request, request.method)
            query = base.filter(**request.GET.dict())
            if query.count == 0:
                return {}
            return {'path': query[0].path,
                    'total': query.aggregate(point=Sum('point'))['point'],
                    'like': base.get_like(method.get('path')),
                    'dislike': base.get_dislike(method.get('path'))}
        return base.all()

    def create(self, request):
        method = getattr(request, request.method)
        base = self.model.objects
        user = None
        if method.get('username'):
            user = method.get('username')

        if method.get('action') == 'dislike':
            r = base.dislike(method.get('path'), user)
        else:
            r = base.like(method.get('path'), user)
        return r


class FavoritedHandler(Handler):
    allowed_methods = ['GET', 'POST']
    model = Favorited

    def create(self, request):
        User = get_user_model()
        method = getattr(request, request.method)
        base = self.model.objects
        user = User.objects.get(username=method.get('api_username'))
        if method.get('unfavorited'):
            query = base.get(path=method.get('path'), user=user)
            query.delete()
        else:
            query = base.get_or_create(path=method.get('path'), user=user)
        return query
