#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LikedManager(models.Manager):

    def _action(self, container, point):
        return super(LikedManager, self).create(
            container=container,
            point=point
        )

    def _get(self, container, operator):
        filters = {}
        filters['container'] = container
        if operator:
            filters['point__{}'.format(operator)] = 0
        query = super(LikedManager, self).get_query_set().filter(
            **filters
        )
        return query.aggregate(total=models.Sum('point'))['total']

    def get_like(self, container):
        return self._get(container, "gt")

    def like(self, container, point=1):
        if point <= 0:
            raise _(u"Point must be positive.")
        return self._action(container, point)

    def dislike(self, container, point=-1):
        if point >= 0:
            raise _(u"Point must be negative.")
        return self._action(container, point)

    def get_dislike(self, container):
        return abs(self._get(container, "lt"))

    def get_total(self, container):
        return self._get(container, None)
