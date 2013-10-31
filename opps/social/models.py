#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from opps.core.models import NotUserPublishable, Publishable

from .managers import LikedManager


class Liked(NotUserPublishable):
    container = models.ForeignKey('containers.Container')
    point = models.IntegerField()
    objects = LikedManager()


class Favorited(Publishable):
    container = models.OneToOneField('containers.Container',
                                     primary_key=True)


