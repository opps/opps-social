#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from opps.core.models import OwnedNotRequired, Owned

from .managers import LikedManager


class Liked(OwnedNotRequired):
    path = models.CharField(max_length=255, db_index=True)
    point = models.IntegerField(db_index=True)
    objects = LikedManager()

    def __unicode__(self):
        return u"{} - {}".format(self.id, self.path)


class Favorited(Owned):
    path = models.CharField(max_length=255, db_index=True)

    def __unicode__(self):
        return u"{} - {}".format(self.id, self.path)

    class Meta:
        unique_together = ("user", "path")
