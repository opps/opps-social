#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()


class LikedManager(models.Manager):

    def _action(self, path, user, point):
        if user:
            try:
                user = User.objects.get(username=user)
            except:
                user = None
        return super(LikedManager, self).create(
            path=path,
            point=point,
            user=user
        )

    def _get(self, path, operator):
        filters = {}
        filters['path'] = path
        if operator:
            filters['point__{}'.format(operator)] = 0
        query = super(LikedManager, self).get_query_set().filter(
            **filters
        )
        return query.aggregate(total=models.Sum('point'))['total']

    def get_like(self, path):
        return self._get(path, "gt")

    def like(self, path, user=None, point=1):
        if point <= 0:
            raise _(u"Point must be positive.")
        return self._action(path, user, point)

    def dislike(self, path, user=None, point=-1):
        if point >= 0:
            raise _(u"Point must be negative.")
        return self._action(path, user, point)

    def get_dislike(self, path):
        ret = self._get(path, "lt")
        if not ret:
            return 0
        return abs(ret)

    def get_total(self, path):
        return self._get(path, None)
