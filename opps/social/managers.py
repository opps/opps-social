#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LikedManager(models.Manager):

    def _action(self, path, point):
        return super(LikedManager, self).create(
            path=path,
            point=point
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

    def like(self, path, point=1):
        if point <= 0:
            raise _(u"Point must be positive.")
        return self._action(path, point)

    def dislike(self, path, point=-1):
        if point >= 0:
            raise _(u"Point must be negative.")
        return self._action(path, point)

    def get_dislike(self, path):
        ret = self._get(path, "lt")
        if not ret:
            return 0
        return abs(ret)

    def get_total(self, path):
        return self._get(path, None)
