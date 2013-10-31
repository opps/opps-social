#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class LikedManager(models.Manager):

    def _action(self, container, point):
        return super(LikedManager, self).create(
            container=container,
            point=point
        )

    def like(self, container, point=1):
        if point <= 0:
            raise _(u"Point must be positive.")
        return self._action(container, point)

    def dislike(self, container, point=-1):
        if point >= 0:
            raise _(u"Point must be negative.")
        return self._action(container, point)
